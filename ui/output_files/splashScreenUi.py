# -*- coding: utf-8 -*-
# Splash Screen — Neon Speakeasy UI (PySide6)

from PySide6 import QtCore, QtGui, QtWidgets
from ui.output_files.icons import (
    WHITE_HOUSE, WHITE_WINE, WHITE_MARTINI, WHITE_MUSIC, WHITE_GEAR,
    CORAL_MARTINI,
)

BG       = "rgb(8, 10, 18)"
CARD_BG  = "rgb(14, 17, 32)"
BORDER   = "rgb(28, 33, 58)"
CORAL    = "rgb(255, 75, 90)"
TEXT_PRI = "rgb(230, 232, 245)"
TEXT_SEC = "rgb(140, 145, 175)"
TEXT_DIM = "rgb(75, 80, 115)"


def _icon_img(path: str, size: int = 22) -> str:
    return f"""
        image: url("{path}");
        min-width: {size}px; min-height: {size}px;
        max-width: {size}px; max-height: {size}px;
        background: transparent; border: none;
    """


class Ui_BartenderSplashScreen(object):

    def setupUi(self, BartenderSplashScreen):
        BartenderSplashScreen.setObjectName("BartenderSplashScreen")
        BartenderSplashScreen.setStyleSheet(f"QWidget {{ background-color: {BG}; }}")

        root = QtWidgets.QVBoxLayout(BartenderSplashScreen)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Hero ──────────────────────────────────────────────────────────
        hero = QtWidgets.QWidget()
        hero.setStyleSheet(f"""
            QWidget {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(16, 10, 24), stop:1 {BG});
            }}
        """)
        hero_lay = QtWidgets.QVBoxLayout(hero)
        hero_lay.setContentsMargins(40, 30, 40, 18)
        hero_lay.setSpacing(6)

        # Large martini icon
        big_icon = QtWidgets.QLabel()
        big_icon.setFixedSize(60, 60)
        big_icon.setStyleSheet(f"QLabel {{ {_icon_img(CORAL_MARTINI, 60)} }}")
        big_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        hero_lay.addWidget(big_icon, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        title = QtWidgets.QLabel("BARTENDER")
        f = QtGui.QFont()
        f.setPointSize(34)
        f.setBold(True)
        title.setFont(f)
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {CORAL}; background: transparent; letter-spacing: 10px;")
        hero_lay.addWidget(title)

        tagline = QtWidgets.QLabel("AUTOMATED COCKTAIL SYSTEM  ·  6 PUMPS")
        f2 = QtGui.QFont()
        f2.setPointSize(8)
        tagline.setFont(f2)
        tagline.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        tagline.setStyleSheet(f"color: {TEXT_DIM}; background: transparent; letter-spacing: 3px;")
        hero_lay.addWidget(tagline)

        # Diamond divider
        div_w = QtWidgets.QWidget()
        div_w.setStyleSheet("background: transparent;")
        div_row = QtWidgets.QHBoxLayout(div_w)
        div_row.setContentsMargins(60, 8, 60, 8)
        div_row.setSpacing(0)
        for side in range(2):
            line = QtWidgets.QFrame()
            line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            line.setStyleSheet(f"background: {BORDER}; max-height: 1px; border: none;")
            if side == 0:
                div_row.addWidget(line, 1)
                dot = QtWidgets.QLabel("◆")
                dot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                dot.setStyleSheet(f"color: {CORAL}; font-size: 9pt; background: transparent; padding: 0 8px;")
                div_row.addWidget(dot)
            else:
                div_row.addWidget(line, 1)
        hero_lay.addWidget(div_w)

        prompt = QtWidgets.QLabel("Select a destination below to begin")
        f3 = QtGui.QFont()
        f3.setPointSize(9)
        f3.setItalic(True)
        prompt.setFont(f3)
        prompt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        prompt.setStyleSheet(f"color: {TEXT_SEC}; background: transparent;")
        hero_lay.addWidget(prompt)

        root.addWidget(hero, 55)

        # ── Nav legend cards ──────────────────────────────────────────────
        legend_bg = QtWidgets.QWidget()
        legend_bg.setStyleSheet(f"QWidget {{ background-color: {BG}; }}")
        leg_lay = QtWidgets.QHBoxLayout(legend_bg)
        leg_lay.setContentsMargins(18, 10, 18, 20)
        leg_lay.setSpacing(10)

        nav_items = [
            (WHITE_HOUSE,   "HOME",    "Return\nhome"),
            (WHITE_WINE,    "DRINKS",  "Premade\nrecipes"),
            (WHITE_MARTINI, "CUSTOM",  "Build\nyour own"),
            (WHITE_MUSIC,   "MUSIC",   "Spotify\ncontrol"),
            (WHITE_GEAR,    "CONFIG",  "Pump\nsetup"),
        ]

        for icon_path, name, desc in nav_items:
            card = QtWidgets.QFrame()
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: {CARD_BG};
                    border: 1px solid {BORDER};
                    border-radius: 10px;
                }}
            """)
            cl = QtWidgets.QVBoxLayout(card)
            cl.setContentsMargins(8, 10, 8, 10)
            cl.setSpacing(4)

            ic = QtWidgets.QLabel()
            ic.setFixedSize(28, 28)
            ic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            ic.setStyleSheet(f"QLabel {{ {_icon_img(icon_path, 28)} }}")
            cl.addWidget(ic, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

            nl = QtWidgets.QLabel(name)
            nf = QtGui.QFont()
            nf.setPointSize(7)
            nf.setBold(True)
            nl.setFont(nf)
            nl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            nl.setStyleSheet(f"color: {CORAL}; background: transparent; border: none; letter-spacing: 1px;")
            cl.addWidget(nl)

            dl = QtWidgets.QLabel(desc)
            df = QtGui.QFont()
            df.setPointSize(7)
            dl.setFont(df)
            dl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            dl.setStyleSheet(f"color: {TEXT_DIM}; background: transparent; border: none;")
            cl.addWidget(dl)

            leg_lay.addWidget(card, 1)

        root.addWidget(legend_bg, 45)

        self.retranslateUi(BartenderSplashScreen)
        QtCore.QMetaObject.connectSlotsByName(BartenderSplashScreen)

    def retranslateUi(self, BartenderSplashScreen):
        BartenderSplashScreen.setWindowTitle("Bartender")
