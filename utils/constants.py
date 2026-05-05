from enum import Enum

FLOW_RATE = 60.0/100.0  # .6
PUMP_CONFIG_PATH = "./utils/pump_config.json"
PREMADE_DRINKS_PATH = "./utils/premade_drinks.json"

class LiquidType(Enum):
    ALCOHOL = "Alcohol"
    MIXER   = "Mixer"

class StrengthLevel(Enum):
    INVALID     = -1
    EASY_TIGER  = 35
    FIFTY_FIFTY = 50
    LITTY_TITTY = 65
    ADIOS_MF    = 80
    MIXER_LEVEL = 260

import os as _os
_PHOSPHOR_WHITE = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), "..", "ui", "images", "phosphor_white"))
_ICON_PAUSE = _os.path.join(_PHOSPHOR_WHITE, "pause.svg").replace("\\", "/")
_ICON_PLAY  = _os.path.join(_PHOSPHOR_WHITE, "play.svg").replace("\\", "/")

_PLAYPAUSE_BASE = """
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 230, 180), stop:1 rgb(0, 170, 130));
    color: rgb(0, 30, 22);
    border: none;
    border-radius: 28px;
    min-width: 56px;
    min-height: 56px;
    max-width: 56px;
    max-height: 56px;
    image: url("{icon}");
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgb(0, 255, 200), stop:1 rgb(0, 200, 155));
}}
QPushButton:pressed {{
    background: rgb(0, 140, 108);
}}
"""

SPOTIFY_PLAY_STATE_STYLE   = _PLAYPAUSE_BASE.format(icon=_ICON_PAUSE)
SPOTIFY_PAUSED_STATE_STYLE = _PLAYPAUSE_BASE.format(icon=_ICON_PLAY)
SPOTIFY_TAB_STYLE = ""  # Tab styling handled inline in spotifyUi.py