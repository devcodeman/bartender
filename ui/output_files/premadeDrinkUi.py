# -*- coding: utf-8 -*-
# Premade Drinks Widget — Neon Speakeasy UI (PySide6)

from PySide6 import QtCore, QtGui, QtWidgets
from ui.output_files.icons import (
    CORAL_WINE,
    WHITE_DROP, WHITE_LIGHTNING, WHITE_FIRE, WHITE_SKULL,
)

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

LIST_STYLE = f"""
QListWidget {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 8px;
    color: {TEXT_PRI};
    font-size: 11pt;
    outline: none;
    padding: 4px 0px;
}}
QListWidget::item {{
    padding: 11px 16px;
    border-bottom: 1px solid {BORDER};
    border-left: 3px solid transparent;
}}
QListWidget::item:hover {{
    background-color: {RAISED};
    border-left: 3px solid {BORDER_H};
}}
QListWidget::item:selected {{
    background-color: rgb(38, 10, 14);
    border-left: 3px solid {CORAL};
    color: rgb(255, 145, 155);
}}
QScrollBar:vertical {{
    background: {CARD_BG}; width: 4px; border-radius: 2px;
}}
QScrollBar::handle:vertical {{
    background: {BORDER_H}; border-radius: 2px; min-height: 20px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
"""

BROWSER_STYLE = f"""
QTextBrowser {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 8px;
    color: {TEXT_SEC};
    font-size: 10pt;
    padding: 14px;
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
    padding-top: 8px;
    background-color: {CARD_BG};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 10px;
    color: {TEXT_DIM};
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
    max-height: 20px;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {CORAL_D}, stop:1 {CORAL});
    border-radius: 3px;
}}
"""

MAKE_BTN_STYLE = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 90, 105), stop:1 rgb(210, 55, 70));
    color: rgb(255, 235, 235);
    border: none;
    border-radius: 8px;
    font-size: 11pt;
    font-weight: bold;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(255, 110, 125), stop:1 rgb(230, 70, 85));
}}
QPushButton:pressed {{
    background: rgb(180, 45, 58);
}}
"""


def _strength_radio_style(color: str) -> str:
    return f"""
        QRadioButton {{
            color: {TEXT_DIM};
            spacing: 0px;
            background: transparent;
            padding: 3px 0px;
        }}
        QRadioButton::indicator {{ width: 0px; height: 0px; }}
        QRadioButton:checked {{ color: {color}; }}
        QRadioButton:hover {{ color: {TEXT_SEC}; }}
    """


def _header_icon(path: str) -> QtWidgets.QLabel:
    lbl = QtWidgets.QLabel()
    lbl.setFixedSize(18, 18)
    lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    lbl.setStyleSheet(f"""
        QLabel {{
            image: url("{path}");
            min-width: 18px; min-height: 18px;
            max-width: 18px; max-height: 18px;
            background: transparent; border: none;
        }}
    """)
    return lbl


class Ui_PremadeDrinksWidget(object):

    def setupUi(self, PremadeDrinksWidget):
        PremadeDrinksWidget.setObjectName("PremadeDrinksWidget")
        PremadeDrinksWidget.setStyleSheet(
            f"QWidget {{ background-color: {BG}; color: {TEXT_PRI}; }}"
            f"QLabel {{ color: {TEXT_PRI}; background: transparent; }}"
        )

        root = QtWidgets.QVBoxLayout(PremadeDrinksWidget)
        root.setContentsMargins(16, 14, 16, 12)
        root.setSpacing(12)

        # ── Header row ────────────────────────────────────────────────────
        hdr = QtWidgets.QHBoxLayout()
        hdr.addWidget(_header_icon(CORAL_WINE))
        hdr.addSpacing(6)

        self.premadeDrinkListLabel = QtWidgets.QLabel("DRINK MENU")
        f = QtGui.QFont(); f.setPointSize(11); f.setBold(True)
        f.setPointSize(12)
        self.premadeDrinkListLabel.setFont(f)
        self.premadeDrinkListLabel.setStyleSheet(f"color: {TEXT_PRI};")
        hdr.addWidget(self.premadeDrinkListLabel)
        hdr.addStretch(1)

        self.premadeDrinkDetailsLabel = QtWidgets.QLabel("INGREDIENTS")
        f2 = QtGui.QFont(); f2.setPointSize(8)
        self.premadeDrinkDetailsLabel.setFont(f2)
        self.premadeDrinkDetailsLabel.setStyleSheet(f"color: {TEXT_DIM};")
        hdr.addWidget(self.premadeDrinkDetailsLabel)
        root.addLayout(hdr)

        # ── List + Details ────────────────────────────────────────────────
        content = QtWidgets.QHBoxLayout()
        content.setSpacing(10)

        self.premadeDrinksList = QtWidgets.QListWidget()
        self.premadeDrinksList.setStyleSheet(LIST_STYLE)
        content.addWidget(self.premadeDrinksList, 55)

        self.premadeDrinkDetailsTextBrowser = QtWidgets.QTextBrowser()
        self.premadeDrinkDetailsTextBrowser.setStyleSheet(BROWSER_STYLE)
        self.premadeDrinkDetailsTextBrowser.setReadOnly(True)
        content.addWidget(self.premadeDrinkDetailsTextBrowser, 45)

        root.addLayout(content, 45)

        # ── Strength + Make ───────────────────────────────────────────────
        bottom = QtWidgets.QHBoxLayout()
        bottom.setSpacing(10)

        self.strengthLevelGroupBox = QtWidgets.QGroupBox("STRENGTH")
        self.strengthLevelGroupBox.setStyleSheet(GROUPBOX_STYLE)
        f3 = QtGui.QFont(); f3.setPointSize(8); f3.setBold(True)
        self.strengthLevelGroupBox.setFont(f3)
        sg = QtWidgets.QHBoxLayout(self.strengthLevelGroupBox)
        sg.setContentsMargins(8, 18, 8, 8)
        sg.setSpacing(4)

        self.easyTigerStrengthLevel  = QtWidgets.QRadioButton("EASY\nTIGER")
        self.fiftyFiftyStrengthLevel = QtWidgets.QRadioButton("50 /\n50")
        self.littyTittyStrengthLevel = QtWidgets.QRadioButton("LITTY\nTITTY")
        self.adioMfStrengthLevel     = QtWidgets.QRadioButton("ADIOS\nMF!")

        strength_cfg = [
            (self.easyTigerStrengthLevel,  WHITE_DROP,      "rgb(80, 160, 255)"),
            (self.fiftyFiftyStrengthLevel, WHITE_LIGHTNING, "rgb(255, 210, 0)"),
            (self.littyTittyStrengthLevel, WHITE_FIRE,      "rgb(255, 140, 30)"),
            (self.adioMfStrengthLevel,     WHITE_SKULL,     "rgb(255, 60, 60)"),
        ]

        rb_group = QtWidgets.QButtonGroup(self.strengthLevelGroupBox)
        for rb, icon_path, color in strength_cfg:
            col_w = QtWidgets.QWidget()
            col_w.setStyleSheet("background: transparent;")
            col_l = QtWidgets.QVBoxLayout(col_w)
            col_l.setContentsMargins(0, 0, 0, 0)
            col_l.setSpacing(3)

            ic = QtWidgets.QLabel()
            ic.setFixedSize(20, 20)
            ic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            ic.setStyleSheet(f"""
                QLabel {{
                    image: url("{icon_path}");
                    min-width: 20px; min-height: 20px;
                    max-width: 20px; max-height: 20px;
                    background: transparent; border: none;
                }}
            """)
            col_l.addWidget(ic, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

            rf = QtGui.QFont(); rf.setPointSize(7)
            rb.setFont(rf)
            rb.setStyleSheet(_strength_radio_style(color))
            rb_group.addButton(rb)
            col_l.addWidget(rb, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
            sg.addWidget(col_w, 1)

        bottom.addWidget(self.strengthLevelGroupBox, 65)

        self.makePremadeDrinkButton = QtWidgets.QPushButton("MAKE\nDRINK")
        self.makePremadeDrinkButton.setStyleSheet(MAKE_BTN_STYLE)
        self.makePremadeDrinkButton.setMinimumHeight(96)
        mf = QtGui.QFont(); mf.setPointSize(12); mf.setBold(True)
        self.makePremadeDrinkButton.setFont(mf)
        bottom.addWidget(self.makePremadeDrinkButton, 35)

        root.addLayout(bottom, 42)

        self.premadeDrinkProgressBar = QtWidgets.QProgressBar()
        self.premadeDrinkProgressBar.setValue(0)
        self.premadeDrinkProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.premadeDrinkProgressBar.setStyleSheet(PROGRESS_STYLE)
        self.premadeDrinkProgressBar.setFixedHeight(24)
        self.premadeDrinkProgressBar.hide()
        root.addWidget(self.premadeDrinkProgressBar)

        self.retranslateUi(PremadeDrinksWidget)
        QtCore.QMetaObject.connectSlotsByName(PremadeDrinksWidget)

    def retranslateUi(self, PremadeDrinksWidget):
        PremadeDrinksWidget.setWindowTitle("Premade Drinks")
        self.premadeDrinkListLabel.setText("DRINK MENU")
        self.premadeDrinkDetailsLabel.setText("INGREDIENTS")
        self.strengthLevelGroupBox.setTitle("STRENGTH")
        self.easyTigerStrengthLevel.setText("EASY\nTIGER")
        self.fiftyFiftyStrengthLevel.setText("50 /\n50")
        self.littyTittyStrengthLevel.setText("LITTY\nTITTY")
        self.adioMfStrengthLevel.setText("ADIOS\nMF!")
        self.makePremadeDrinkButton.setText("MAKE\nDRINK")
