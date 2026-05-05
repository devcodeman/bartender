# Bartender — Brand Guidelines

A cocktail-pouring Raspberry Pi kiosk. The UI runs full-screen on a touchscreen and should feel like stepping up to a sleek bar at night: dark, warm, and inviting — not a sterile tech dashboard.

---

## Personality

- **Confident & playful.** The strength levels are named "Easy Tiger", "Fifty Fifty", "Litty Titty", and "Adios MF" — the UI should match that energy.
- **Approachable.** A guest hands you their phone at a party, not a developer. Tap targets are large, flows are short, labels are plain English.
- **Ambient.** Think low lighting, neon reflections on a wet bar top. Nothing harsh or clinical.

---

## Color Palette

### Backgrounds

| Role | Value | Notes |
|------|-------|-------|
| App background | `#0A0F0D` | Near-black, slightly green-tinted |
| Surface / card | `#111A16` | One step up from background |
| Elevated surface | `#1A2820` | Modals, panels, active states |
| Divider / border | `#1F3029` | Subtle, barely there |

### Accent — Mint (Primary)

The primary brand color. Used on primary CTAs, progress indicators, and active nav items.

| Role | Value |
|------|-------|
| Mint 500 (default) | `#00E6B4` → `rgb(0, 230, 180)` |
| Mint 600 (hover) | `#00FFC8` → `rgb(0, 255, 200)` |
| Mint 700 (pressed) | `#008C6C` → `rgb(0, 140, 108)` |
| Mint gradient stop 0 | `rgb(0, 230, 180)` |
| Mint gradient stop 1 | `rgb(0, 170, 130)` |
| Mint on-color text | `rgb(0, 30, 22)` — very dark green, use on mint backgrounds |

### Accent — Coral (Secondary)

Use for warnings, destructive actions, and secondary highlights (e.g. "Adios MF" strength tier).

| Role | Value |
|------|-------|
| Coral 500 | `#FF6B6B` |
| Coral 600 (hover) | `#FF8E8E` |

### Neutrals

| Role | Value |
|------|-------|
| Text primary | `#E8F5F0` |
| Text secondary | `#8AB5A0` |
| Text disabled / dim | `#4A6B5C` |

---

## Typography

The app targets a touchscreen kiosk — favor legibility over decoration.

| Role | Size | Weight | Notes |
|------|------|--------|-------|
| Screen title | 28–32px | 700 | e.g. "Premade Drinks" |
| Section label | 18–20px | 600 | e.g. "Ingredients" |
| Body / drink name | 16px | 400 | List items, descriptions |
| Caption / metadata | 13px | 400 | Secondary info |
| Button label | 15–16px | 600 | All-caps optional |

**Font stack:** `"Inter", "SF Pro Display", system-ui, sans-serif`

---

## Iconography

Icons come from the [Phosphor Icons](https://phosphoricons.com/) set and live under `ui/images/`. Four tinted variants are available:

| Variant | Path | Use for |
|---------|------|---------|
| White | `ui/images/phosphor_white/` | Default / active nav |
| Mint | `ui/images/phosphor_mint/` | Highlighted / CTA icons |
| Coral | `ui/images/phosphor_coral/` | Warning / destructive icons |
| Dim | `ui/images/phosphor_dim/` | Inactive / disabled state |

**Available icons:** `beer-bottle`, `check-square`, `download-simple`, `drop`, `faders`, `fire`, `gear`, `house`, `lightning`, `list`, `magnifying-glass`, `martini`, `music-notes`, `pause`, `play`, `queue`, `shuffle`, `skip-back`, `skip-forward`, `skull`

Icon sizes: **24px** inline, **32px** nav bar, **56px** media transport (play/pause).

---

## Components

### Primary Button

```
Background: linear-gradient(to bottom, #00E6B4, #00AA82)
Color: rgb(0, 30, 22)
Border: none
Border-radius: 12px
Padding: 14px 28px
Font: 16px / 600
```

Hover → lighten gradient stops by ~10%.  
Pressed → flat `#008C6C`.  
Disabled → `#1F3029` background, `#4A6B5C` text.

### Destructive / Secondary Button

```
Background: transparent
Border: 1.5px solid #FF6B6B
Color: #FF6B6B
Border-radius: 12px
Padding: 14px 28px
```

### List Item (drinks list)

```
Background: #111A16
Border-radius: 10px
Padding: 12px 16px
Spacing between items: 7px
Active/selected: border-left 3px solid #00E6B4, background #1A2820
```

### Progress Bar

Mint fill on a dark track (`#1A2820`). Centered label text in `#E8F5F0`. Height: 20px, border-radius: 10px.

### Cards / Panels

```
Background: #111A16
Border: 1px solid #1F3029
Border-radius: 14px
Padding: 20px
```

### Navigation Bar

Full-width bottom or side rail. Active tab: icon in white + mint underline or mint dot indicator. Inactive: dim icon, no label or faded label.

---

## Motion

Keep it subtle — this runs on a Pi.

| Interaction | Duration | Easing |
|-------------|----------|--------|
| Button press | 80ms | ease-out |
| Page / widget transition | 180ms | ease-in-out |
| Progress bar fill | linear, driven by real pour time | — |

Avoid large-scale animations or blur effects that could lag on embedded hardware.

---

## Tone of Voice (UI copy)

- Use bar/bartender metaphors in progress messages and empty states.
- Playful but not juvenile. Match the strength-level names.
- Short. A touchscreen user is standing — no paragraphs.

**Examples:**
- Empty drinks list → *"Nothing on tap — check your pump configuration."*
- Saving settings → *"Locking it in."*
- Progress stages → follow the existing sequence: *"Getting bartender's attention… Placing order… Hittin' on the cuties ;)… Pouring your drink… Enjoy!"*

---

## Do / Don't

| Do | Don't |
|----|-------|
| Dark backgrounds, mint accents | Light / white backgrounds |
| Large tap targets (min 48px) | Small links or dense tables |
| Phosphor icon set (existing variants) | Mixed icon libraries |
| Coral for warnings only | Coral as a decorative accent |
| Plain English labels | Jargon or abbreviations |
| Subtle gradients on CTAs | Flat grey buttons that disappear into the background |
