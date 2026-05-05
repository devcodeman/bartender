# -*- coding: utf-8 -*-
# Custom Drink Widget — Neon Speakeasy UI (PySide6)

from PySide6 import QtCore, QtGui, QtWidgets

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

WIDGET_STYLE = f"""
QWidget {{
    background-color: {BG};
    color: {TEXT_PRI};
}}
QLabel {{
    color: {TEXT_PRI};
    background: transparent;
}}
"""

GROUPBOX_STYLE = f"""
QGroupBox {{
    color: {TEXT_DIM};
    font-size: 8pt;
    font-weight: bold;
    border: 1px solid {BORDER};
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 4px;
    background-color: {CARD_BG};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 10px;
    color: {TEXT_DIM};
}}
"""

CHECKBOX_STYLE = f"""
QCheckBox {{
    color: {TEXT_PRI};
    font-size: 12pt;
    spacing: 12px;
    padding: 8px 4px;
    background: transparent;
}}
QCheckBox::indicator {{
    width: 22px;
    height: 22px;
    border-radius: 5px;
    border: 2px solid {BORDER_H};
    background-color: {RAISED};
}}
QCheckBox::indicator:hover {{
    border-color: {CORAL};
    background-color: rgb(35, 12, 16);
}}
QCheckBox::indicator:checked {{
    background-color: {CORAL};
    border-color: {CORAL};
}}
"""

PROGRESS_STYLE = f"""
QProgressBar {{
    background-color: {RAISED};
    border: none;
    border-radius: 3px;
    text-align: center;
    color: {TEXT_PRI};
    font-size: 8pt;
    max-height: 24px;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {CORAL_D}, stop:1 {CORAL});
    border-radius: 3px;
}}
"""

PRIMARY_BTN = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 90, 105), stop:1 rgb(210, 55, 70));
    color: rgb(255, 235, 235);
    border: none;
    border-radius: 8px;
    font-size: 13pt;
    font-weight: bold;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 110, 125), stop:1 rgb(230, 70, 85));
}}
QPushButton:pressed {{ background: rgb(180, 45, 58); }}
"""

SECONDARY_BTN = f"""
QPushButton {{
    background-color: {RAISED};
    color: {TEXT_SEC};
    border: 1px solid {BORDER_H};
    border-radius: 8px;
    font-size: 11pt;
    font-weight: bold;
}}
QPushButton:hover {{
    border-color: {CORAL};
    color: {TEXT_PRI};
    background-color: rgb(28, 20, 30);
}}
QPushButton:pressed {{ background-color: rgb(35, 12, 16); }}
"""

# Strength radio buttons styled as pill toggles — no images needed
def _strength_style(color: str) -> str:
    return f"""
        QRadioButton {{
            color: {TEXT_DIM};
            font-size: 10pt;
            font-weight: bold;
            spacing: 0px;
            padding: 10px 6px;
            background: {RAISED};
            border: 1px solid {BORDER};
            border-radius: 8px;
        }}
        QRadioButton::indicator {{
            width: 0px;
            height: 0px;
        }}
        QRadioButton:hover {{
            color: {TEXT_PRI};
            border-color: {color};
            background: rgb(20, 22, 40);
        }}
        QRadioButton:checked {{
            color: {color};
            border: 2px solid {color};
            background: rgb(16, 18, 34);
        }}
    """


class Ui_CustomDrinkWidget(object):

    def setupUi(self, CustomDrinkWidget):
        CustomDrinkWidget.setObjectName("CustomDrinkWidget")
        CustomDrinkWidget.setStyleSheet(WIDGET_STYLE)

        root = QtWidgets.QVBoxLayout(CustomDrinkWidget)
        root.setContentsMargins(16, 12, 16, 12)
        root.setSpacing(10)

        # ── Header ────────────────────────────────────────────────────────
        hdr = QtWidgets.QHBoxLayout()
        page_title = QtWidgets.QLabel("BUILD YOUR DRINK")
        hf = QtGui.QFont(); hf.setPointSize(13); hf.setBold(True)
        page_title.setFont(hf)
        page_title.setStyleSheet(f"color: {TEXT_PRI};")
        hdr.addWidget(page_title)
        hdr.addStretch(1)
        root.addLayout(hdr)

        # ── Drink options ─────────────────────────────────────────────────
        self.drinkOptionsGroupBox = QtWidgets.QGroupBox("SELECT INGREDIENTS")
        self.drinkOptionsGroupBox.setStyleSheet(GROUPBOX_STYLE)
        gf = QtGui.QFont(); gf.setPointSize(8); gf.setBold(True)
        self.drinkOptionsGroupBox.setFont(gf)

        gl = QtWidgets.QGridLayout(self.drinkOptionsGroupBox)
        gl.setContentsMargins(20, 20, 20, 12)
        gl.setSpacing(4)
        gl.setHorizontalSpacing(24)

        self.drinkOption1 = QtWidgets.QCheckBox("Pump 1")
        self.drinkOption2 = QtWidgets.QCheckBox("Pump 2")
        self.drinkOption3 = QtWidgets.QCheckBox("Pump 3")
        self.drinkOption4 = QtWidgets.QCheckBox("Pump 4")
        self.drinkOption5 = QtWidgets.QCheckBox("Pump 5")
        self.drinkOption6 = QtWidgets.QCheckBox("Pump 6")

        cbf = QtGui.QFont(); cbf.setPointSize(12)
        for cb in [self.drinkOption1, self.drinkOption2, self.drinkOption3,
                   self.drinkOption4, self.drinkOption5, self.drinkOption6]:
            cb.setStyleSheet(CHECKBOX_STYLE)
            cb.setFont(cbf)
            cb.setMinimumHeight(48)

        gl.addWidget(self.drinkOption1, 0, 0)
        gl.addWidget(self.drinkOption2, 1, 0)
        gl.addWidget(self.drinkOption3, 0, 1)
        gl.addWidget(self.drinkOption4, 1, 1)
        gl.addWidget(self.drinkOption5, 0, 2)
        gl.addWidget(self.drinkOption6, 1, 2)
        gl.setColumnStretch(0, 1)
        gl.setColumnStretch(1, 1)
        gl.setColumnStretch(2, 1)

        self.customDrinkHelpLabel = QtWidgets.QLabel(
            "Go to Config to update pump assignments")
        hintf = QtGui.QFont(); hintf.setPointSize(8); hintf.setItalic(True)
        self.customDrinkHelpLabel.setFont(hintf)
        self.customDrinkHelpLabel.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customDrinkHelpLabel.setStyleSheet(
            f"color: {TEXT_DIM}; border: none;")
        gl.addWidget(self.customDrinkHelpLabel, 2, 0, 1, 3)

        root.addWidget(self.drinkOptionsGroupBox, 42)

        # ── Strength ──────────────────────────────────────────────────────
        self.strengthLevelGroupBox = QtWidgets.QGroupBox("STRENGTH")
        self.strengthLevelGroupBox.setStyleSheet(GROUPBOX_STYLE)
        self.strengthLevelGroupBox.setFont(gf)

        sg = QtWidgets.QHBoxLayout(self.strengthLevelGroupBox)
        sg.setContentsMargins(12, 18, 12, 12)
        sg.setSpacing(8)

        self.easyTigerStrengthLevel  = QtWidgets.QRadioButton("🧊  Easy Tiger")
        self.fiftyFiftyStrengthLevel = QtWidgets.QRadioButton("⚡  50 / 50")
        self.littyTittyStrengthLevel = QtWidgets.QRadioButton("🔥  Litty Titty")
        self.adioMfStrengthLevel     = QtWidgets.QRadioButton("💀  ADIOS MF!")

        strength_cfg = [
            (self.easyTigerStrengthLevel,  "rgb(80, 160, 255)"),
            (self.fiftyFiftyStrengthLevel, "rgb(255, 210, 0)"),
            (self.littyTittyStrengthLevel, "rgb(255, 140, 30)"),
            (self.adioMfStrengthLevel,     "rgb(255, 60, 60)"),
        ]

        rb_group = QtWidgets.QButtonGroup(self.strengthLevelGroupBox)
        sf = QtGui.QFont(); sf.setPointSize(10); sf.setBold(True)
        for rb, color in strength_cfg:
            rb.setFont(sf)
            rb.setStyleSheet(_strength_style(color))
            rb.setMinimumHeight(52)
            rb_group.addButton(rb)
            sg.addWidget(rb, 1)

        root.addWidget(self.strengthLevelGroupBox, 30)

        # ── Action buttons ────────────────────────────────────────────────
        act = QtWidgets.QHBoxLayout()
        act.setSpacing(10)

        self.saveCustomDrinkButton = QtWidgets.QPushButton("💾  Save")
        self.saveCustomDrinkButton.setStyleSheet(SECONDARY_BTN)
        self.saveCustomDrinkButton.setMinimumHeight(58)
        sf2 = QtGui.QFont(); sf2.setPointSize(11); sf2.setBold(True)
        self.saveCustomDrinkButton.setFont(sf2)

        self.clearCustomDrinkButton = QtWidgets.QPushButton("✕  Clear")
        self.clearCustomDrinkButton.setStyleSheet(SECONDARY_BTN)
        self.clearCustomDrinkButton.setMinimumHeight(58)
        self.clearCustomDrinkButton.setFont(sf2)

        self.makeCustomDrinkButton = QtWidgets.QPushButton("🍸  Mix It!")
        self.makeCustomDrinkButton.setStyleSheet(PRIMARY_BTN)
        self.makeCustomDrinkButton.setMinimumHeight(58)
        mf = QtGui.QFont(); mf.setPointSize(13); mf.setBold(True)
        self.makeCustomDrinkButton.setFont(mf)

        # Hidden labels kept for API compatibility with customDrinkWidget.py
        self.saveLabel  = QtWidgets.QLabel(); self.saveLabel.hide()
        self.clearLabel = QtWidgets.QLabel(); self.clearLabel.hide()
        self.mixItLabel = QtWidgets.QLabel(); self.mixItLabel.hide()

        act.addWidget(self.saveCustomDrinkButton,  1)
        act.addWidget(self.clearCustomDrinkButton, 1)
        act.addWidget(self.makeCustomDrinkButton,  2)
        root.addLayout(act, 24)

        # ── Progress bar ──────────────────────────────────────────────────
        self.customDrinkProgressBar = QtWidgets.QProgressBar()
        self.customDrinkProgressBar.setValue(0)
        self.customDrinkProgressBar.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customDrinkProgressBar.setStyleSheet(PROGRESS_STYLE)
        self.customDrinkProgressBar.setFixedHeight(24)
        self.customDrinkProgressBar.hide()
        root.addWidget(self.customDrinkProgressBar)

        self.retranslateUi(CustomDrinkWidget)
        QtCore.QMetaObject.connectSlotsByName(CustomDrinkWidget)

    def retranslateUi(self, CustomDrinkWidget):
        CustomDrinkWidget.setWindowTitle("Custom Drink")
        self.drinkOptionsGroupBox.setTitle("SELECT INGREDIENTS")
        self.strengthLevelGroupBox.setTitle("STRENGTH")
        self.easyTigerStrengthLevel.setText("🧊  Easy Tiger")
        self.fiftyFiftyStrengthLevel.setText("⚡  50 / 50")
        self.littyTittyStrengthLevel.setText("🔥  Litty Titty")
        self.adioMfStrengthLevel.setText("💀  ADIOS MF!")
        self.saveCustomDrinkButton.setText("💾  Save")
        self.clearCustomDrinkButton.setText("✕  Clear")
        self.makeCustomDrinkButton.setText("🍸  Mix It!")
