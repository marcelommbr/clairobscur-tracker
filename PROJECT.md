# Clair Obscur: Expedition 33 — Achievement Tracker

## Overview

A mobile-first, single-page web app for tracking in-game achievements in *Clair Obscur: Expedition 33*. Built with Vanilla JS, hosted on GitHub Pages. All data is static (JSON) and all progress is persisted to `localStorage` with optional JSON export for backup.

---

## Goals

- Track completion of all achievement categories across a full playthrough
- Flag missable/act-locked items so nothing is permanently skipped
- Show cross-checklist relationships (e.g. a Picto won from an Optional Boss)
- Work comfortably on a smartphone in both portrait and landscape orientations
- Respect the visual art direction of the game: dark, painterly, elegant

---

## Stack

| Layer | Choice | Reason |
|---|---|---|
| Language | Vanilla JS (ES modules) | No build step, lightweight, GitHub Pages ready |
| Styling | CSS custom properties + CSS Grid/Flex | Art-directed without a framework |
| Data | Static JSON files | One file per checklist category |
| Storage | `localStorage` | Zero-backend persistence |
| Export | JSON download via Blob URL | Simple backup/restore |
| Hosting | GitHub Pages | Free, static, no server needed |

---

## Project Structure

```
/
├── index.html
├── style.css
├── app.js                   # Entry point, router, state management
├── components/
│   ├── Header.js            # Title, progress ring, nav icons
│   ├── CategoryPage.js      # Category selector (full-screen overlay)
│   ├── FilterDropdown.js    # Filter panel (status, act, missable)
│   ├── CategorySection.js   # Section header + progress bar + item list
│   ├── ChecklistItem.js     # Collapsed row / expanded card
│   └── CrossRef.js          # Inline cross-reference badge
├── data/
│   ├── categories.json      # Category metadata (id, name, icon, color)
│   ├── optional-bosses.json
│   ├── pictos.json
│   ├── side-quests.json
│   ├── main-story.json
│   ├── exploration.json
│   └── ...                  # One file per category
├── assets/
│   ├── fonts/
│   ├── icons/               # SVG icons for UI actions
│   └── images/              # Game art assets (header bg, category images)
└── PROJECT.md
```

---

## UX Design

### Mobile-First Layout

- Single-column layout optimized for 375–430px wide screens
- No persistent sidebar — all navigation is icon-based in the header
- Touch targets minimum 44×44px

### Header

```
[ Clair Obscur ] ——————— [🗂 Category] [⚙ Filter] [↓ Export]
[ Overall progress bar ]
```

- **Category icon** → full-screen overlay listing all categories with per-category progress
- **Filter icon** → dropdown panel: filter by completion status (All / Done / Remaining), act (1/2/3), missable flag
- **Export icon** → downloads progress as `clairobscur-progress.json`

### Category Sections (main scroll)

Each active category renders as:

```
━━ [Category Name] ━━━━━━━━━━━━ 12 / 34 ━━
▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 35%

[ ] Task Name          Location      ⚠ Missable
[ ] Task Name          Location
...
```

### Checklist Item — Collapsed State

Single-line row showing:
- Checkbox (left)
- Task name
- Location (truncated)
- Missable badge (⚠) if applicable
- Act badge (Act 1 / Act 2 / Act 3) if restricted

### Checklist Item — Expanded State

Tapping any row expands an inline card:

```
┌─────────────────────────────────────────┐
│ ☑  Task Name                   ⚠ Act 2 │
│ Location: Valley of Sighs               │
│                                         │
│ Description: Full description text...   │
│                                         │
│ Rewards: Lumina ×3, [Picto: Lumière ✓] │
│                                         │
│ [↗ IGN Walkthrough]                     │
└─────────────────────────────────────────┘
```

- Only one item can be expanded at a time (accordion behavior)
- Tapping the expanded item or elsewhere collapses it

### Cross-Checklist References

When a reward or description mentions an item tracked in another checklist (e.g. a Picto dropped by an Optional Boss), it renders as an inline badge:

```
[Picto: Lumière ✓]   ← green if already collected
[Picto: Ombre  ○]    ← grey if not yet collected
```

Tapping a cross-ref badge scrolls to that item in its own category section.

### Missable / Act-Locked Items

- **Missable**: orange ⚠ badge on collapsed row; warning text in expanded card
- **Act-locked**: grey pill badge showing "Act 1 only" / "Act 2" / "Act 3"
- Items locked to a past act are visually dimmed if the user has marked that act as completed (future enhancement: act progress tracker in header)

---

## Data Format

Each category JSON file follows this schema:

```json
{
  "id": "optional-bosses",
  "name": "Optional Bosses",
  "icon": "sword",
  "color": "#8B3A8B",
  "items": [
    {
      "id": "ob-001",
      "name": "The Forgotten Warden",
      "location": "Valley of Sighs",
      "act": 2,
      "missable": true,
      "description": "Full description of how to find and defeat this boss.",
      "rewards": [
        { "type": "picto", "ref": "picto-042", "name": "Lumière" },
        { "type": "item", "name": "Warden's Blade" }
      ],
      "ign_url": "https://www.ign.com/wikis/clair-obscur-expedition-33/..."
    }
  ]
}
```

---

## State Management

All state lives in a single JS object persisted to `localStorage`:

```js
{
  "version": 1,
  "completed": {               // Set of completed item IDs
    "ob-001": true,
    "picto-042": true
  },
  "filters": {
    "status": "all",           // "all" | "done" | "remaining"
    "act": null,               // null | 1 | 2 | 3
    "missable": false
  },
  "activeCategory": null       // null = show all, or category id
}
```

---

## Visual Design Direction

### Palette

| Role | Color |
|---|---|
| Background | `#0d0b14` (near-black, deep purple-dark) |
| Surface | `#1a1526` |
| Surface elevated | `#241e33` |
| Accent primary | `#c9a96e` (warm gold) |
| Accent secondary | `#7b5ea7` (muted violet) |
| Text primary | `#f0e8d8` (warm off-white) |
| Text secondary | `#9b8fa8` (muted lavender-grey) |
| Success / completed | `#5a9e6f` (muted green) |
| Warning / missable | `#d4824a` (amber-orange) |
| Danger | `#b84c4c` |

### Typography

- **Headings**: serif font with painterly character (e.g. *Cormorant Garamond* or *IM Fell English* from Google Fonts)
- **Body / UI**: clean sans-serif for readability (e.g. *Inter* or *DM Sans*)
- Mixed serif/sans creates the "elegant but legible" tone

### Texture & Atmosphere

- Subtle noise/grain overlay on the background (CSS filter or SVG feTurbulence)
- Category headers use a faint decorative rule (CSS border with gradient)
- Progress bars styled as painted brushstrokes (CSS clip-path or SVG)
- Checkbox uses a custom SVG stamp/seal aesthetic instead of a browser default

---

## Checklist Categories (to be finalized in CHECKLISTS.md)

| Category | Est. Items | Has Rewards Col | Notes |
|---|---|---|---|
| Main Story | ~30 | No | Act-ordered, none missable |
| Optional Bosses | ~20 | Yes | Missable possible, drop Pictos |
| Side Quests | ~25 | No | Some act-locked |
| Pictos | ~80 | No | Cross-ref from Bosses/Quests |
| Luminas | ~50 | No | Crafted from Pictos |
| Exploration | ~40 | No | Collectibles, landmarks |
| Combat Achievements | ~15 | No | Challenge-based |

*Exact numbers to be confirmed after CHECKLISTS.md research.*

---

## Milestones

1. `PROJECT.md` — this document ✓
2. `CHECKLISTS.md` — sourced achievement data
3. `TASKS.md` — implementation tasks
4. GitHub repo setup
5. Core shell (HTML/CSS, data loading, localStorage)
6. Header + navigation
7. Category sections + checklist items
8. Cross-reference system
9. Filters + export
10. Polish, testing on mobile
