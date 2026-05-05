# -*- coding: utf-8 -*-
# Spotify Widget — Neon Speakeasy UI (PySide6)

from PySide6 import QtCore, QtGui, QtWidgets
from ui.output_files.icons import (
    CORAL_MUSIC,
    MINT_PLAY, MINT_PAUSE, MINT_SKIP_FWD, MINT_SKIP_BAK,
    WHITE_SEARCH, WHITE_PLAY, WHITE_SKIP_FWD, WHITE_SKIP_BAK,
)

BG       = "rgb(8, 10, 18)"
CARD_BG  = "rgb(13, 16, 28)"
RAISED   = "rgb(20, 24, 42)"
CORAL    = "rgb(255, 75, 90)"
MINT     = "rgb(0, 210, 160)"
MINT_D   = "rgb(0, 150, 115)"
TEXT_PRI = "rgb(230, 232, 245)"
TEXT_SEC = "rgb(140, 145, 175)"
TEXT_DIM = "rgb(75, 80, 115)"
BORDER   = "rgb(28, 33, 58)"
BORDER_H = "rgb(50, 55, 90)"

TAB_STYLE = f"""
QTabWidget::pane {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER};
    border-top: none;
    border-radius: 0px 0px 8px 8px;
}}
QTabBar {{ background: transparent; }}
QTabBar::tab {{
    background-color: {RAISED};
    color: {TEXT_DIM};
    border: 1px solid {BORDER};
    border-bottom: none;
    border-radius: 6px 6px 0 0;
    padding: 7px 0px;
    min-width: 90px;
    font-size: 8pt;
    font-weight: bold;
    margin-right: 3px;
}}
QTabBar::tab:selected {{
    background-color: {CARD_BG};
    color: {MINT};
    border-bottom: 2px solid {MINT};
}}
QTabBar::tab:hover:!selected {{
    color: {TEXT_SEC};
    background-color: rgb(18, 22, 40);
}}
"""

LIST_STYLE = f"""
QListWidget {{
    background-color: {CARD_BG};
    border: none;
    color: {TEXT_PRI};
    font-size: 10pt;
    outline: none;
    padding: 4px 0;
}}
QListWidget::item {{
    padding: 10px 14px;
    border-bottom: 1px solid {BORDER};
    border-left: 3px solid transparent;
}}
QListWidget::item:hover {{ background-color: {RAISED}; }}
QListWidget::item:selected {{
    background-color: rgb(0, 35, 28);
    border-left: 3px solid {MINT};
    color: rgb(100, 235, 195);
}}
QScrollBar:vertical {{
    background: {CARD_BG}; width: 4px; border-radius: 2px;
}}
QScrollBar::handle:vertical {{
    background: {BORDER_H}; border-radius: 2px; min-height: 20px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
"""

SEARCH_INPUT_STYLE = f"""
QLineEdit {{
    background-color: {RAISED};
    color: {TEXT_PRI};
    border: none;
    border-bottom: 2px solid {BORDER_H};
    font-size: 10pt;
    padding: 6px 10px;
    selection-background-color: {MINT};
    selection-color: rgb(0, 0, 0);
}}
QLineEdit:focus {{ border-bottom: 2px solid {MINT}; }}
"""

SEARCH_BTN_STYLE = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 230, 180), stop:1 rgb(0, 170, 130));
    color: rgb(0, 30, 22);
    border: none;
    border-radius: 4px;
    font-size: 9pt;
    font-weight: bold;
    min-height: 40px;
    padding: 0 16px;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 255, 200), stop:1 rgb(0, 200, 155));
}}
QPushButton:pressed {{ background: rgb(0, 140, 108); }}
"""

TRANSPORT_BTN = f"""
QPushButton {{
    background-color: {RAISED};
    border: 1px solid {BORDER};
    border-radius: 26px;
    min-width: 52px; min-height: 52px;
    max-width: 52px; max-height: 52px;
    padding: 10px;
}}
QPushButton:hover {{
    background-color: rgb(0, 35, 28);
    border-color: {MINT};
}}
QPushButton:pressed {{ background-color: rgb(0, 50, 40); }}
"""

PLAYPAUSE_BTN = f"""
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 230, 180), stop:1 rgb(0, 170, 130));
    border: none;
    border-radius: 34px;
    min-width: 68px; min-height: 68px;
    max-width: 68px; max-height: 68px;
    padding: 14px;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 255, 200), stop:1 rgb(0, 200, 155));
}}
QPushButton:pressed {{ background: rgb(0, 140, 108); }}
"""


class Ui_SpotifyWidget(object):

    def setupUi(self, SpotifyWidget):
        SpotifyWidget.setObjectName("SpotifyWidget")
        SpotifyWidget.setStyleSheet(
            f"QWidget {{ background-color: {BG}; color: {TEXT_PRI}; }}"
            f"QLabel {{ color: {TEXT_PRI}; background: transparent; }}"
        )

        root = QtWidgets.QVBoxLayout(SpotifyWidget)
        root.setContentsMargins(14, 12, 14, 10)
        root.setSpacing(10)

        # ── Header with inline now-playing ────────────────────────────────
        hdr = QtWidgets.QHBoxLayout()
        ic = QtWidgets.QLabel()
        ic.setFixedSize(18, 18)
        ic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        ic.setStyleSheet(f"""
            QLabel {{
                image: url("{CORAL_MUSIC}");
                min-width: 18px; min-height: 18px;
                max-width: 18px; max-height: 18px;
                background: transparent; border: none;
            }}
        """)
        hdr.addWidget(ic)
        hdr.addSpacing(6)

        page_title = QtWidgets.QLabel("MUSIC CONTROL")
        ptf = QtGui.QFont(); ptf.setPointSize(11); ptf.setBold(True)
        page_title.setFont(ptf)
        page_title.setStyleSheet(f"color: {TEXT_PRI};")
        hdr.addWidget(page_title)
        hdr.addStretch(1)

        self.currentlyPlayingLabel_2 = QtWidgets.QLabel("NOW PLAYING")
        np2f = QtGui.QFont(); np2f.setPointSize(7)
        self.currentlyPlayingLabel_2.setFont(np2f)
        self.currentlyPlayingLabel_2.setStyleSheet(f"color: {MINT};")
        hdr.addWidget(self.currentlyPlayingLabel_2)
        hdr.addSpacing(6)

        self.currentlyPlayingLabel = QtWidgets.QLabel("—")
        npf = QtGui.QFont(); npf.setPointSize(9); npf.setItalic(True)
        self.currentlyPlayingLabel.setFont(npf)
        self.currentlyPlayingLabel.setStyleSheet(f"color: {TEXT_SEC};")
        self.currentlyPlayingLabel.setMaximumWidth(200)
        hdr.addWidget(self.currentlyPlayingLabel)
        root.addLayout(hdr)

        # ── Tabs ──────────────────────────────────────────────────────────
        self.spotifyTabWidget = QtWidgets.QTabWidget()
        self.spotifyTabWidget.setObjectName("spotifyTabWidget")
        self.spotifyTabWidget.setStyleSheet(TAB_STYLE)

        # Search tab
        self.spotifySearchTab = QtWidgets.QWidget()
        self.spotifySearchTab.setObjectName("spotifySearchTab")
        self.spotifySearchTab.setStyleSheet(f"QWidget {{ background-color: {CARD_BG}; }}")
        sl = QtWidgets.QVBoxLayout(self.spotifySearchTab)
        sl.setContentsMargins(10, 10, 10, 8)
        sl.setSpacing(8)

        sbar = QtWidgets.QHBoxLayout()
        sbar.setSpacing(8)
        self.spotifySearchInputField = QtWidgets.QLineEdit()
        self.spotifySearchInputField.setObjectName("spotifySearchInputField")
        self.spotifySearchInputField.setPlaceholderText("Search songs, artists, albums…")
        self.spotifySearchInputField.setMinimumHeight(40)
        self.spotifySearchInputField.setStyleSheet(SEARCH_INPUT_STYLE)
        sif = QtGui.QFont(); sif.setPointSize(10)
        self.spotifySearchInputField.setFont(sif)
        sbar.addWidget(self.spotifySearchInputField, 1)

        self.spotifySearchButton = QtWidgets.QPushButton("SEARCH")
        self.spotifySearchButton.setObjectName("spotifySearchButton")
        self.spotifySearchButton.setStyleSheet(SEARCH_BTN_STYLE)
        sbf = QtGui.QFont(); sbf.setPointSize(9); sbf.setBold(True)
        self.spotifySearchButton.setFont(sbf)
        sbar.addWidget(self.spotifySearchButton)
        sl.addLayout(sbar)

        self.spotifySearchResultsField = QtWidgets.QListWidget()
        self.spotifySearchResultsField.setObjectName("spotifySearchResultsField")
        self.spotifySearchResultsField.setStyleSheet(LIST_STYLE)
        rf = QtGui.QFont(); rf.setPointSize(10)
        self.spotifySearchResultsField.setFont(rf)
        sl.addWidget(self.spotifySearchResultsField)

        self.spotifyTabWidget.addTab(self.spotifySearchTab, "SEARCH")

        # Queue tab
        self.spotifyQueueTab = QtWidgets.QWidget()
        self.spotifyQueueTab.setObjectName("spotifyQueueTab")
        self.spotifyQueueTab.setStyleSheet(f"QWidget {{ background-color: {CARD_BG}; }}")
        ql = QtWidgets.QVBoxLayout(self.spotifyQueueTab)
        ql.setContentsMargins(10, 10, 10, 8)
        ql.setSpacing(6)

        qh = QtWidgets.QLabel("BARTENDER QUEUE")
        qhf = QtGui.QFont(); qhf.setPointSize(8); qhf.setBold(True)
        qh.setFont(qhf)
        qh.setStyleSheet(f"color: {MINT};")
        ql.addWidget(qh)

        self.spotifyQueueField = QtWidgets.QListWidget()
        self.spotifyQueueField.setObjectName("spotifyQueueField")
        self.spotifyQueueField.setStyleSheet(LIST_STYLE)
        self.spotifyQueueField.setFont(rf)
        ql.addWidget(self.spotifyQueueField)

        self.spotifyTabWidget.addTab(self.spotifyQueueTab, "QUEUE")
        root.addWidget(self.spotifyTabWidget, 1)

        # ── Transport controls ────────────────────────────────────────────
        trans_bg = QtWidgets.QWidget()
        trans_bg.setStyleSheet(f"""
            QWidget {{
                background-color: {CARD_BG};
                border: 1px solid {BORDER};
                border-radius: 8px;
            }}
        """)
        tl = QtWidgets.QHBoxLayout(trans_bg)
        tl.setContentsMargins(16, 10, 16, 10)
        tl.setSpacing(0)
        tl.addStretch(1)

        self.spotifyPreviousButton = QtWidgets.QPushButton()
        self.spotifyPreviousButton.setObjectName("spotifyPreviousButton")
        self.spotifyPreviousButton.setFixedSize(52, 52)
        self.spotifyPreviousButton.setStyleSheet(
            TRANSPORT_BTN + f'QPushButton {{ image: url("{WHITE_SKIP_BAK}"); }}'
        )
        tl.addWidget(self.spotifyPreviousButton)
        tl.addSpacing(16)

        self.spotifyPlayPauseButton = QtWidgets.QPushButton()
        self.spotifyPlayPauseButton.setObjectName("spotifyPlayPauseButton")
        self.spotifyPlayPauseButton.setFixedSize(68, 68)
        self.spotifyPlayPauseButton.setStyleSheet(
            PLAYPAUSE_BTN + f'QPushButton {{ image: url("{WHITE_PLAY}"); }}'
        )
        tl.addWidget(self.spotifyPlayPauseButton)
        tl.addSpacing(16)

        self.spotifyNextButton = QtWidgets.QPushButton()
        self.spotifyNextButton.setObjectName("spotifyNextButton")
        self.spotifyNextButton.setFixedSize(52, 52)
        self.spotifyNextButton.setStyleSheet(
            TRANSPORT_BTN + f'QPushButton {{ image: url("{WHITE_SKIP_FWD}"); }}'
        )
        tl.addWidget(self.spotifyNextButton)
        tl.addStretch(1)

        root.addWidget(trans_bg)

        self.retranslateUi(SpotifyWidget)
        QtCore.QMetaObject.connectSlotsByName(SpotifyWidget)

    def retranslateUi(self, SpotifyWidget):
        SpotifyWidget.setWindowTitle("Music")
        self.spotifySearchInputField.setPlaceholderText("Search songs, artists, albums…")
        self.spotifySearchButton.setText("SEARCH")
        self.spotifyTabWidget.setTabText(0, "SEARCH")
        self.spotifyTabWidget.setTabText(1, "QUEUE")
        self.currentlyPlayingLabel_2.setText("NOW PLAYING")
        self.currentlyPlayingLabel.setText("—")
