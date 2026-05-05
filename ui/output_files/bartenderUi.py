# -*- coding: utf-8 -*-
# Bartender Main Window — Neon Speakeasy UI (PySide6)

from PySide6 import QtCore, QtGui, QtWidgets
from ui.output_files.icons import (
    DIM_HOUSE, DIM_WINE, DIM_MARTINI, DIM_MUSIC, DIM_GEAR,
    CORAL_HOUSE, CORAL_WINE, CORAL_MARTINI, CORAL_MUSIC, CORAL_GEAR,
)

BG        = "rgb(8, 10, 18)"
DOCK_BG   = "rgb(11, 13, 23)"
DOCK_LINE = "rgb(28, 33, 58)"
CORAL     = "rgb(255, 75, 90)"
CORAL_DIM = "rgb(140, 40, 50)"
TEXT_PRI  = "rgb(230, 232, 245)"
TEXT_DIM  = "rgb(90, 95, 130)"

MAIN_STYLE = f"""
QMainWindow {{ background-color: {BG}; }}
QWidget#centralwidget {{ background-color: {BG}; }}
QMenuBar {{ background-color: {BG}; color: {TEXT_DIM}; }}
QStatusBar {{ background-color: {BG}; color: {TEXT_DIM}; border: none; }}
"""

ICON_SIZE = 26   # px for dock SVG icons
TEXT_PT   = 8    # pt for dock labels


class _DockButton(QtWidgets.QWidget):
    """
    Dock nav button: SVG icon centred above a text label.
    Exposes a .clicked Signal so bartender.py's .clicked.connect() works unchanged.
    Inherits QWidget (not QAbstractButton) to avoid the pure-virtual paintEvent trap.
    """

    clicked = QtCore.Signal()

    def __init__(self, dim_icon: str, active_icon: str, label: str, parent=None):
        super().__init__(parent)
        self._dim_icon    = dim_icon
        self._active_icon = active_icon
        self._border_color = QtGui.QColor(0, 0, 0, 0)  # transparent

        self.setFixedHeight(72)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("background: transparent;")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 8)
        layout.setSpacing(4)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._icon_lbl = QtWidgets.QLabel()
        self._icon_lbl.setFixedSize(ICON_SIZE, ICON_SIZE)
        self._icon_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._icon_lbl.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self._set_icon(dim_icon)
        layout.addWidget(self._icon_lbl, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self._text_lbl = QtWidgets.QLabel(label.upper())
        self._text_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._text_lbl.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        f = QtGui.QFont()
        f.setPointSize(TEXT_PT)
        self._text_lbl.setFont(f)
        self._text_lbl.setStyleSheet(f"color: {TEXT_DIM}; background: transparent; border: none;")
        layout.addWidget(self._text_lbl, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

    def _set_icon(self, path: str):
        self._icon_lbl.setStyleSheet(f"""
            QLabel {{
                image: url("{path}");
                min-width: {ICON_SIZE}px; min-height: {ICON_SIZE}px;
                max-width: {ICON_SIZE}px; max-height: {ICON_SIZE}px;
                background: transparent; border: none;
            }}
        """)

    def _set_state(self, hover: bool, pressed: bool):
        if pressed:
            self._set_icon(self._active_icon)
            self._text_lbl.setStyleSheet(f"color: {CORAL}; background: transparent; border: none;")
            self._border_color = QtGui.QColor(CORAL)
        elif hover:
            self._set_icon(self._active_icon)
            self._text_lbl.setStyleSheet(f"color: {TEXT_PRI}; background: transparent; border: none;")
            self._border_color = QtGui.QColor(CORAL_DIM)
        else:
            self._set_icon(self._dim_icon)
            self._text_lbl.setStyleSheet(f"color: {TEXT_DIM}; background: transparent; border: none;")
            self._border_color = QtGui.QColor(0, 0, 0, 0)
        self.update()

    def paintEvent(self, event):
        # Draw background then top accent line — no super() call needed for QWidget
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), QtGui.QColor(11, 13, 23))
        if self._border_color.alpha() > 0:
            painter.setPen(QtGui.QPen(self._border_color, 2))
            painter.drawLine(0, 1, self.width(), 1)
        painter.end()

    def enterEvent(self, event):
        self._set_state(hover=True, pressed=False)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._set_state(hover=False, pressed=False)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._set_state(hover=False, pressed=True)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._set_state(hover=False, pressed=False)
            self.clicked.emit()
        super().mouseReleaseEvent(event)


class Ui_BartenderUI(object):

    def setupUi(self, BartenderUI):
        BartenderUI.setObjectName("BartenderUI")
        BartenderUI.setFixedSize(800, 480)
        BartenderUI.setStyleSheet(MAIN_STYLE)
        BartenderUI.setWindowTitle("Bartender")

        self.centralwidget = QtWidgets.QWidget(BartenderUI)
        self.centralwidget.setObjectName("centralwidget")

        root = QtWidgets.QVBoxLayout(self.centralwidget)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Content stacked widget ─────────────────────────────────────────
        self.mainDisplayWidget = QtWidgets.QStackedWidget()
        self.mainDisplayWidget.setObjectName("mainDisplayWidget")
        self.mainDisplayWidget.setStyleSheet(
            f"QStackedWidget {{ background-color: {BG}; border: none; }}"
        )
        root.addWidget(self.mainDisplayWidget, 1)

        # ── Bottom dock ────────────────────────────────────────────────────
        dock = QtWidgets.QWidget()
        dock.setObjectName("dock")
        dock.setFixedHeight(72)
        dock.setStyleSheet(f"""
            QWidget#dock {{
                background-color: {DOCK_BG};
                border-top: 1px solid {DOCK_LINE};
            }}
        """)
        dock_layout = QtWidgets.QHBoxLayout(dock)
        dock_layout.setContentsMargins(0, 0, 0, 0)
        dock_layout.setSpacing(0)

        self.homeButton          = _DockButton(DIM_HOUSE,   CORAL_HOUSE,   "Home")
        self.premadeDrinksButton = _DockButton(DIM_WINE,    CORAL_WINE,    "Drinks")
        self.customDrinkButton   = _DockButton(DIM_MARTINI, CORAL_MARTINI, "Custom")
        self.spotifyButton       = _DockButton(DIM_MUSIC,   CORAL_MUSIC,   "Music")
        self.settingsButton      = _DockButton(DIM_GEAR,    CORAL_GEAR,    "Config")

        for btn in [self.homeButton, self.premadeDrinksButton,
                    self.customDrinkButton, self.spotifyButton, self.settingsButton]:
            dock_layout.addWidget(btn, 1)

        root.addWidget(dock)

        self.menubar = QtWidgets.QMenuBar(BartenderUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 0))
        self.menubar.setVisible(False)
        self.statusbar = QtWidgets.QStatusBar(BartenderUI)
        self.statusbar.setVisible(False)

        BartenderUI.setCentralWidget(self.centralwidget)
        BartenderUI.setMenuBar(self.menubar)
        BartenderUI.setStatusBar(self.statusbar)

        self.retranslateUi(BartenderUI)
        QtCore.QMetaObject.connectSlotsByName(BartenderUI)

    def retranslateUi(self, BartenderUI):
        BartenderUI.setWindowTitle("Bartender")
