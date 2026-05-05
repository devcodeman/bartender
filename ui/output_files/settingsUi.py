# -*- coding: utf-8 -*-
# Settings Widget — Neon Speakeasy UI (PySide6)
# Pump configuration via touchscreen scroll-wheel pickers, no keyboard needed.

import random
from PySide6 import QtCore, QtGui, QtWidgets
from ui.output_files.icons import CORAL_FADERS

BG       = "rgb(8, 10, 18)"
CARD_BG  = "rgb(13, 16, 28)"
RAISED   = "rgb(20, 24, 42)"
CORAL    = "rgb(255, 75, 90)"
CORAL_D  = "rgb(180, 52, 63)"
TEXT_PRI = "rgb(230, 232, 245)"
TEXT_SEC = "rgb(140, 145, 175)"
TEXT_DIM = "rgb(75, 80, 115)"
BORDER   = "rgb(28, 33, 58)"
BORDER_H = "rgb(50, 55, 90)"

# ── Liquid catalogue ───────────────────────────────────────────────────────
# (emoji, display name, value stored in config)
LIQUIDS = [
    # ── Spirits ───────────────────────────────────────────────────────────
    ("🍸", "Gin",                 "gin"),
    ("🥃", "Whiskey",             "whiskey"),
    ("🍶", "Vodka",               "vodka"),
    ("🍹", "Rum",                 "rum"),
    ("🌵", "Tequila",             "tequila"),
    ("🥂", "Champagne",           "champagne"),
    ("🍷", "Wine",                "wine"),
    ("🔥", "Bourbon",             "bourbon"),
    ("🧊", "Scotch",              "scotch"),
    ("🌿", "Midori",              "midori"),
    ("🍑", "Peach Schnapps",      "peach schnapps"),
    ("🫐", "Blueberry Schnapps", "blueberry schnapps"),
    ("🍊", "Triple Sec",          "triple sec"),
    ("🌺", "Aperol",              "aperol"),
    ("🇮🇹", "Amaretto",           "amaretto"),
    ("🫒", "Vermouth",            "vermouth"),
    ("🌾", "Sake",                "sake"),
    # ── Mixers ────────────────────────────────────────────────────────────
    ("🥤", "Coke",                "coke"),
    ("🫧", "Club Soda",           "club soda"),
    ("🍋", "Tonic",               "tonic"),
    ("🍊", "Orange Juice",        "orange juice"),
    ("🍍", "Pineapple Juice",     "pineapple juice"),
    ("💧", "Sparkling Water",     "sparkling water"),
    ("🍒", "Grenadine",           "grenadine"),
    ("🫙", "Simple Syrup",        "simple syrup"),
    ("🥛", "Cream",               "cream"),
    ("☕", "Coffee",              "coffee"),
    ("🍵", "Ginger Beer",         "ginger beer"),
    ("🫗", "Lemonade",            "lemonade"),
]

# ── Slot machine timing ────────────────────────────────────────────────────
# Each tick interval in ms for each phase: fast spin → decelerate → land
_SPIN_PHASES = [
    # (interval_ms, ticks)
    (40,  18),   # fast spin
    (60,  6),    # slight slowdown
    (90,  4),    # more slowdown
    (130, 3),    # crawl
    (180, 2),    # nearly stopped
    (240, 1),    # last tick before landing
]

# ── Styles ─────────────────────────────────────────────────────────────────
ARROW_BTN = f"""
QPushButton {{
    background-color: {RAISED};
    color: {TEXT_SEC};
    border: 1px solid {BORDER};
    border-radius: 5px;
    font-size: 10pt;
    min-height: 26px;
    max-height: 26px;
    padding: 0px;
}}
QPushButton:hover {{
    background-color: rgb(30, 15, 18);
    border-color: {CORAL};
    color: {CORAL};
}}
QPushButton:pressed {{
    background-color: rgb(50, 20, 25);
}}
"""

RANDOMIZE_BTN = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 rgb(120, 30, 40), stop:1 rgb(80, 18, 26));
    color: {CORAL};
    border: 1px solid {CORAL_D};
    border-radius: 8px;
    font-size: 10pt;
    font-weight: bold;
    min-height: 40px;
    padding: 0 20px;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 rgb(160, 40, 55), stop:1 rgb(110, 25, 35));
    border-color: {CORAL};
    color: rgb(255, 200, 205);
}}
QPushButton:pressed {{
    background: rgb(60, 14, 20);
}}
QPushButton:disabled {{
    background: rgb(25, 14, 18);
    color: {TEXT_DIM};
    border-color: {BORDER};
}}
"""

SAVE_BTN = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 90, 105), stop:1 rgb(210, 55, 70));
    color: rgb(255, 235, 235);
    border: none;
    border-radius: 6px;
    font-size: 9pt;
    font-weight: bold;
    min-width: 110px;
    min-height: 40px;
    padding: 0 16px;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 110, 125), stop:1 rgb(230, 70, 85));
}}
QPushButton:pressed {{ background: rgb(180, 45, 58); }}
"""

DISCARD_BTN = f"""
QPushButton {{
    background-color: transparent;
    color: {TEXT_DIM};
    border: 1px solid {BORDER_H};
    border-radius: 6px;
    font-size: 9pt;
    font-weight: bold;
    min-width: 110px;
    min-height: 40px;
    padding: 0 16px;
}}
QPushButton:hover {{
    border-color: rgb(180, 60, 60);
    color: rgb(255, 100, 100);
}}
QPushButton:pressed {{ background-color: rgb(20, 8, 8); }}
"""


# ── Font helper ───────────────────────────────────────────────────────────
def _font(pt: int, bold: bool = False) -> QtGui.QFont:
    f = QtGui.QFont()
    f.setPointSize(pt)
    f.setBold(bold)
    return f


# ── Scroll picker ──────────────────────────────────────────────────────────

class _ScrollPicker(QtWidgets.QWidget):
    """
    Drum-roll picker built on QScrollArea — every row is exactly _ITEM_H px
    tall by construction, so centering math is pixel-perfect regardless of
    font metrics or widget show/hide order.

    Exposes .text() / .setText() matching QLineEdit API.
    Call .spin_to(target_index) to kick off the slot-machine animation.
    """

    valueChanged = QtCore.Signal(str)
    spinFinished = QtCore.Signal()

    _ITEM_H  = 54
    _VISIBLE = 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self._items    = LIQUIDS
        self._index    = 0
        self._spinning = False
        self._rows: list[QtWidgets.QLabel] = []

        # Slot machine state
        self._spin_target = 0
        self._spin_phase  = 0
        self._spin_ticks  = 0
        self._spin_timer  = QtCore.QTimer(self)
        self._spin_timer.setSingleShot(False)
        self._spin_timer.timeout.connect(self._spin_tick)

        viewport_h = self._ITEM_H * self._VISIBLE
        # height = arrows (26×2) + scroll viewport + name label (36) + gaps
        self.setFixedHeight(viewport_h + 26 + 26 + 36 + 12)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )

        root = QtWidgets.QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(4)

        # ── Up arrow ──────────────────────────────────────────────────────
        self._up_btn = QtWidgets.QPushButton("▲")
        self._up_btn.setStyleSheet(ARROW_BTN)
        self._up_btn.setFixedHeight(26)
        self._up_btn.setFont(_font(11))
        self._up_btn.clicked.connect(self._scroll_up)
        root.addWidget(self._up_btn)

        # ── Scroll area (emoji only) ───────────────────────────────────────
        # widgetResizable=True lets Qt manage the inner widget width to match
        # the viewport — this ensures rows are visible immediately on first show.
        self._scroll = QtWidgets.QScrollArea()
        self._scroll.setFixedHeight(viewport_h)
        self._scroll.setWidgetResizable(True)
        self._scroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._scroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._scroll.setStyleSheet(f"""
            QScrollArea {{
                background-color: {CARD_BG};
                border: 1px solid {BORDER};
                border-radius: 8px;
            }}
            QScrollArea > QWidget > QWidget {{
                background-color: {CARD_BG};
            }}
        """)

        # Inner container — use a VBoxLayout so Qt owns width, we own height.
        # Each row gets a fixed height of _ITEM_H; total height is n * _ITEM_H.
        self._inner = QtWidgets.QWidget()
        inner_layout = QtWidgets.QVBoxLayout(self._inner)
        inner_layout.setContentsMargins(0, 0, 0, 0)
        inner_layout.setSpacing(0)

        # All rows use the same fixed font — selection is shown via
        # background/border only so Qt never needs to re-layout on tick.
        ef_emoji = _font(22)

        for emoji, label, _ in self._items:
            row = QtWidgets.QLabel(emoji)
            row.setFixedHeight(self._ITEM_H)
            row.setSizePolicy(
                QtWidgets.QSizePolicy.Policy.Expanding,
                QtWidgets.QSizePolicy.Policy.Fixed,
            )
            row.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            row.setFont(ef_emoji)
            row.setStyleSheet("background: transparent; border: none;")
            row.setProperty("full_name", label)
            inner_layout.addWidget(row)
            self._rows.append(row)

        self._scroll.setWidget(self._inner)
        root.addWidget(self._scroll)

        # ── Down arrow ────────────────────────────────────────────────────
        self._dn_btn = QtWidgets.QPushButton("▼")
        self._dn_btn.setStyleSheet(ARROW_BTN)
        self._dn_btn.setFixedHeight(26)
        self._dn_btn.setFont(_font(11))
        self._dn_btn.clicked.connect(self._scroll_down)
        root.addWidget(self._dn_btn)

        # ── Selected name label (below picker) ────────────────────────────
        # Word-wrap + smaller font ensures even "Blueberry Schnapps" fits.
        # Fixed height (two line max), Ignored horizontal policy so text
        # changes never trigger a geometry recalculation during spin.
        self._name_label = QtWidgets.QLabel()
        self._name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._name_label.setWordWrap(True)
        self._name_label.setFixedHeight(36)
        self._name_label.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self._name_label.setFont(_font(8, bold=True))
        self._name_label.setStyleSheet(
            f"color: {CORAL}; background: transparent; border: none;")
        root.addWidget(self._name_label)

        self._scroll.installEventFilter(self)

        # ── Long-press tooltip ────────────────────────────────────────────
        self._long_press_timer = QtCore.QTimer(self)
        self._long_press_timer.setSingleShot(True)
        self._long_press_timer.setInterval(500)
        self._long_press_timer.timeout.connect(self._show_long_press_tooltip)
        self._press_pos = QtCore.QPoint()
        self._scroll.viewport().installEventFilter(self)

        self._set_index(0, emit=False)

    # ── Event filter ──────────────────────────────────────────────────────
    def eventFilter(self, obj, event):
        if obj is self._scroll and event.type() == QtCore.QEvent.Type.Resize:
            pass  # widgetResizable=True handles width automatically

        if obj is self._scroll.viewport():
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                if self._spinning:
                    return True
                self._press_pos = event.pos()
                self._long_press_timer.start()
                # Tap to select: find which row was tapped
                row_idx = (event.pos().y() +
                           self._scroll.verticalScrollBar().value()) // self._ITEM_H
                if 0 <= row_idx < len(self._items):
                    self._set_index(row_idx)
            elif event.type() in (
                QtCore.QEvent.Type.MouseButtonRelease,
                QtCore.QEvent.Type.MouseMove,
            ):
                self._long_press_timer.stop()

        return super().eventFilter(obj, event)

    def _show_long_press_tooltip(self):
        # Since full name is always visible in _name_label, tooltip is less
        # critical — but keep it for accessibility / hover confirmation.
        row_idx = (self._press_pos.y() +
                   self._scroll.verticalScrollBar().value()) // self._ITEM_H
        if 0 <= row_idx < len(self._items):
            _, full_name, _ = self._items[row_idx]
            global_pos = self._scroll.viewport().mapToGlobal(self._press_pos)
            QtWidgets.QToolTip.showText(
                global_pos,
                f"<b style='font-size:13pt; color:#ff4b5a;'>{full_name}</b>",
                self._scroll,
            )

    # ── Index / style helpers ─────────────────────────────────────────────
    def _set_index(self, idx: int, emit: bool = True):
        idx = idx % len(self._items)
        self._index = idx
        # Scroll so selected row is centred in the viewport
        centre_offset = (self._VISIBLE // 2) * self._ITEM_H
        target_scroll = idx * self._ITEM_H - centre_offset
        sb = self._scroll.verticalScrollBar()
        self._scroll.verticalScrollBar().setValue(
            max(sb.minimum(), min(target_scroll, sb.maximum())))
        self._update_row_styles(spinning=self._spinning)
        if emit:
            self.valueChanged.emit(self._items[idx][2])

    def _update_row_styles(self, spinning: bool = False):
        border_color = CORAL if spinning else CORAL_D
        for i, row in enumerate(self._rows):
            if i == self._index:
                row.setStyleSheet(
                    f"background: rgb(35,12,16);"
                    f"border-top: 2px solid {border_color};"
                    f"border-bottom: 2px solid {border_color};"
                    f"border-left: none; border-right: none;"
                )
            else:
                row.setStyleSheet("background: transparent; border: none;")
        # Update the name label below the picker
        _, label, _ = self._items[self._index]
        self._name_label.setText(label.upper())

    # ── Manual scroll ────────────────────────────────────────────────────
    def _scroll_up(self):
        if not self._spinning:
            self._set_index(self._index - 1)

    def _scroll_down(self):
        if not self._spinning:
            self._set_index(self._index + 1)

    # ── Slot machine animation ────────────────────────────────────────────
    def spin_to(self, target_index: int):
        if self._spinning:
            return
        self._spinning    = True
        self._spin_target = target_index % len(self._items)
        self._spin_phase  = 0
        self._spin_ticks  = 0
        self._up_btn.setEnabled(False)
        self._dn_btn.setEnabled(False)
        self._update_row_styles(spinning=True)
        interval, _ = _SPIN_PHASES[0]
        self._spin_timer.start(interval)

    def _spin_tick(self):
        self._set_index((self._index + 1) % len(self._items), emit=False)
        self._spin_ticks += 1
        _, phase_ticks = _SPIN_PHASES[self._spin_phase]
        if self._spin_ticks >= phase_ticks:
            self._spin_phase += 1
            self._spin_ticks  = 0
            if self._spin_phase >= len(_SPIN_PHASES):
                self._spin_timer.stop()
                self._land()
                return
            interval, _ = _SPIN_PHASES[self._spin_phase]
            self._spin_timer.setInterval(interval)

    def _land(self):
        self._set_index(self._spin_target, emit=True)
        self._spinning = False
        self._update_row_styles(spinning=False)
        self._up_btn.setEnabled(True)
        self._dn_btn.setEnabled(True)
        self.spinFinished.emit()

    # ── QLineEdit-compatible API ──────────────────────────────────────────
    def text(self) -> str:
        return self._items[self._index][2]

    def setText(self, value: str):
        value = value.strip().lower()
        for i, (_, _, val) in enumerate(self._items):
            if val == value:
                self._set_index(i, emit=False)
                return
        self._set_index(0, emit=False)


# ── Slot machine orchestrator ──────────────────────────────────────────────

class _SlotMachine(QtCore.QObject):
    """
    Orchestrates spinning all 4 pickers in staggered sequence:
    each column starts and stops one at a time, left to right.
    """

    finished = QtCore.Signal()

    # Delay between each column starting its spin (ms)
    _COLUMN_DELAY = 180

    def __init__(self, pickers: list, parent=None):
        super().__init__(parent)
        self._pickers = pickers
        self._targets = []
        self._pending = 0

    def roll(self):
        """Pick random targets and spin all columns staggered."""
        n = len(self._pickers)
        # Sample without replacement — guaranteed all 4 are unique
        self._targets = random.sample(range(len(LIQUIDS)), n)

        self._pending = n

        for col_idx, (picker, target) in enumerate(
            zip(self._pickers, self._targets)
        ):
            picker.spinFinished.connect(self._on_spin_finished)
            delay = col_idx * self._COLUMN_DELAY
            QtCore.QTimer.singleShot(delay, lambda p=picker, t=target: p.spin_to(t))

    def _on_spin_finished(self):
        sender = self.sender()
        if sender:
            try:
                sender.spinFinished.disconnect(self._on_spin_finished)
            except RuntimeError:
                pass
        self._pending -= 1
        if self._pending <= 0:
            self.finished.emit()


# ── Main UI ────────────────────────────────────────────────────────────────

class Ui_SettingsWidget(object):

    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.setStyleSheet(
            f"QWidget {{ background-color: {BG}; color: {TEXT_PRI}; }}"
            f"QLabel  {{ color: {TEXT_PRI}; background: transparent; }}"
        )

        root = QtWidgets.QVBoxLayout(SettingsWidget)
        root.setContentsMargins(16, 12, 16, 12)
        root.setSpacing(10)

        # ── Header ────────────────────────────────────────────────────────
        hdr = QtWidgets.QHBoxLayout()

        ic = QtWidgets.QLabel()
        ic.setFixedSize(18, 18)
        ic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        ic.setStyleSheet(f"""
            QLabel {{
                image: url("{CORAL_FADERS}");
                min-width: 18px; min-height: 18px;
                max-width: 18px; max-height: 18px;
                background: transparent; border: none;
            }}
        """)
        hdr.addWidget(ic)
        hdr.addSpacing(6)

        self.settingsLabel = QtWidgets.QLabel("PUMP CONFIGURATION")
        hf = QtGui.QFont(); hf.setPointSize(11); hf.setBold(True)
        self.settingsLabel.setFont(hf)
        self.settingsLabel.setStyleSheet(f"color: {TEXT_PRI};")
        hdr.addWidget(self.settingsLabel)
        hdr.addStretch(1)

        hint = QtWidgets.QLabel("Hold any item to see full name")
        hintf = QtGui.QFont(); hintf.setPointSize(8); hintf.setItalic(True)
        hint.setFont(hintf)
        hint.setStyleSheet(f"color: {TEXT_DIM};")
        hdr.addWidget(hint)

        root.addLayout(hdr)

        # ── Four pump picker columns ──────────────────────────────────────
        pump_data = [
            ("pump1ConfigurationField", "settingsPumpLabel1", "PUMP 1"),
            ("pump2ConfigurationField", "settingsPumpLabel2", "PUMP 2"),
            ("pump3ConfigurationField", "settingsPumpLabel3", "PUMP 3"),
            ("pump4ConfigurationField", "settingsPumpLabel4", "PUMP 4"),
            ("pump5ConfigurationField", "settingsPumpLabel5", "PUMP 5"),
            ("pump6ConfigurationField", "settingsPumpLabel6", "PUMP 6"),
        ]

        pickers_row = QtWidgets.QHBoxLayout()
        pickers_row.setSpacing(10)

        lf = QtGui.QFont(); lf.setPointSize(8); lf.setBold(True)
        self._pickers = []

        for field_name, lbl_name, lbl_text in pump_data:
            col = QtWidgets.QWidget()
            col.setStyleSheet(f"""
                QWidget {{
                    background-color: {CARD_BG};
                    border: 1px solid {BORDER};
                    border-radius: 10px;
                }}
            """)
            col_layout = QtWidgets.QVBoxLayout(col)
            col_layout.setContentsMargins(8, 10, 8, 10)
            col_layout.setSpacing(8)

            badge = QtWidgets.QLabel(lbl_text)
            badge.setFont(lf)
            badge.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            badge.setStyleSheet(
                f"color: {CORAL}; background: transparent; border: none;")
            badge.setObjectName(lbl_name)
            setattr(self, lbl_name, badge)
            col_layout.addWidget(badge)

            picker = _ScrollPicker()
            picker.setObjectName(field_name)
            setattr(self, field_name, picker)
            col_layout.addWidget(picker)
            self._pickers.append(picker)

            pickers_row.addWidget(col, 1)

        root.addLayout(pickers_row, 1)

        # ── Bottom row: Randomize + Save/Discard ──────────────────────────
        self._slot_machine = _SlotMachine(self._pickers, SettingsWidget)
        self._slot_machine.finished.connect(self._on_slots_finished)

        btn_row = QtWidgets.QHBoxLayout()

        # Randomize button
        self._randomize_btn = QtWidgets.QPushButton("🎰  RANDOMIZE")
        self._randomize_btn.setStyleSheet(RANDOMIZE_BTN)
        rbf = QtGui.QFont(); rbf.setPointSize(10); rbf.setBold(True)
        self._randomize_btn.setFont(rbf)
        self._randomize_btn.setMinimumHeight(40)
        self._randomize_btn.clicked.connect(self._start_slots)
        btn_row.addWidget(self._randomize_btn)

        btn_row.addStretch(1)

        self.saveCancelSettingsBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Save
            | QtWidgets.QDialogButtonBox.StandardButton.Discard
        )
        self.saveCancelSettingsBox.setCenterButtons(False)
        self.saveCancelSettingsBox.setStyleSheet(
            "background: transparent; border: none;")

        bf = QtGui.QFont(); bf.setPointSize(10); bf.setBold(True)
        for btn in self.saveCancelSettingsBox.buttons():
            role = self.saveCancelSettingsBox.buttonRole(btn)
            if role == QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole:
                btn.setStyleSheet(SAVE_BTN)
                btn.setText("SAVE")
            else:
                btn.setStyleSheet(DISCARD_BTN)
                btn.setText("DISCARD")
            btn.setFont(bf)

        btn_row.addWidget(self.saveCancelSettingsBox)
        root.addLayout(btn_row)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def _start_slots(self):
        self._randomize_btn.setEnabled(False)
        self._randomize_btn.setText("🎰  SPINNING...")
        self._slot_machine.roll()

    def _on_slots_finished(self):
        self._randomize_btn.setEnabled(True)
        self._randomize_btn.setText("🎰  RANDOMIZE")

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle("Settings")
        self.settingsLabel.setText("PUMP CONFIGURATION")
        for i in range(1, 7):
            getattr(self, f"settingsPumpLabel{i}").setText(f"PUMP {i}")
