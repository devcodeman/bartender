# -*- coding: utf-8 -*-
# Phosphor Icons (MIT License) — https://phosphoricons.com
# Pre-colored SVG variants: dim, coral, mint, white

import os

_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "images"))

def _p(variant: str, name: str) -> str:
    return os.path.join(_BASE, variant, name).replace("\\", "/")


# ── Icon name constants ────────────────────────────────────────────────────
_HOUSE        = "house.svg"
_MARTINI      = "martini.svg"
_WINE         = "wine.svg"
_MUSIC        = "music-notes.svg"
_GEAR         = "gear.svg"
_PLAY         = "play.svg"
_PAUSE        = "pause.svg"
_SKIP_FWD     = "skip-forward.svg"
_SKIP_BACK    = "skip-back.svg"
_SEARCH       = "magnifying-glass.svg"
_QUEUE        = "queue.svg"
_FIRE         = "fire.svg"
_SKULL        = "skull.svg"
_LIGHTNING    = "lightning.svg"
_SAVE         = "download-simple.svg"
_TRASH        = "trash.svg"
_SHUFFLE      = "shuffle.svg"
_DROP         = "drop.svg"
_FADERS       = "faders.svg"
_LIST         = "list.svg"
_BEER         = "beer-bottle.svg"

# ── Dim (inactive / placeholder) ──────────────────────────────────────────
DIM_HOUSE     = _p("phosphor_dim", _HOUSE)
DIM_MARTINI   = _p("phosphor_dim", _MARTINI)
DIM_WINE      = _p("phosphor_dim", _WINE)
DIM_MUSIC     = _p("phosphor_dim", _MUSIC)
DIM_GEAR      = _p("phosphor_dim", _GEAR)
DIM_PLAY      = _p("phosphor_dim", _PLAY)
DIM_PAUSE     = _p("phosphor_dim", _PAUSE)
DIM_FADERS    = _p("phosphor_dim", _FADERS)
DIM_SEARCH    = _p("phosphor_dim", _SEARCH)
DIM_SAVE      = _p("phosphor_dim", _SAVE)
DIM_TRASH     = _p("phosphor_dim", _TRASH)
DIM_SHUFFLE   = _p("phosphor_dim", _SHUFFLE)

# ── Coral (primary accent) ─────────────────────────────────────────────────
CORAL_HOUSE    = _p("phosphor_coral", _HOUSE)
CORAL_MARTINI  = _p("phosphor_coral", _MARTINI)
CORAL_WINE     = _p("phosphor_coral", _WINE)
CORAL_MUSIC    = _p("phosphor_coral", _MUSIC)
CORAL_GEAR     = _p("phosphor_coral", _GEAR)
CORAL_FIRE     = _p("phosphor_coral", _FIRE)
CORAL_SKULL    = _p("phosphor_coral", _SKULL)
CORAL_LIGHTNING= _p("phosphor_coral", _LIGHTNING)
CORAL_DROP     = _p("phosphor_coral", _DROP)
CORAL_FADERS   = _p("phosphor_coral", _FADERS)
CORAL_SAVE     = _p("phosphor_coral", _SAVE)
CORAL_TRASH    = _p("phosphor_coral", _TRASH)
CORAL_SHUFFLE  = _p("phosphor_coral", _SHUFFLE)

# ── Mint (spotify / music accent) ─────────────────────────────────────────
MINT_MUSIC    = _p("phosphor_mint", _MUSIC)
MINT_PLAY     = _p("phosphor_mint", _PLAY)
MINT_PAUSE    = _p("phosphor_mint", _PAUSE)
MINT_SKIP_FWD = _p("phosphor_mint", _SKIP_FWD)
MINT_SKIP_BAK = _p("phosphor_mint", _SKIP_BACK)
MINT_SEARCH   = _p("phosphor_mint", _SEARCH)
MINT_QUEUE    = _p("phosphor_mint", _QUEUE)

# ── White (bright / high visibility) ──────────────────────────────────────
WHITE_HOUSE    = _p("phosphor_white", _HOUSE)
WHITE_MARTINI  = _p("phosphor_white", _MARTINI)
WHITE_WINE     = _p("phosphor_white", _WINE)
WHITE_MUSIC    = _p("phosphor_white", _MUSIC)
WHITE_GEAR     = _p("phosphor_white", _GEAR)
WHITE_PLAY     = _p("phosphor_white", _PLAY)
WHITE_PAUSE    = _p("phosphor_white", _PAUSE)
WHITE_SKIP_FWD = _p("phosphor_white", _SKIP_FWD)
WHITE_SKIP_BAK = _p("phosphor_white", _SKIP_BACK)
WHITE_FIRE     = _p("phosphor_white", _FIRE)
WHITE_SKULL    = _p("phosphor_white", _SKULL)
WHITE_LIGHTNING= _p("phosphor_white", _LIGHTNING)
WHITE_DROP     = _p("phosphor_white", _DROP)
WHITE_FADERS   = _p("phosphor_white", _FADERS)
WHITE_SAVE     = _p("phosphor_white", _SAVE)
WHITE_TRASH    = _p("phosphor_white", _TRASH)
WHITE_SHUFFLE  = _p("phosphor_white", _SHUFFLE)
WHITE_SEARCH   = _p("phosphor_white", _SEARCH)
