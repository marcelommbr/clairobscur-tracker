# Clair Obscur: Expedition 33 — Implementation Tasks

> Design reference: `design/option-1-dark-canvas.html`  
> Stack: Vanilla JS (ES modules) · CSS custom properties · Static JSON · localStorage  
> Hosting: GitHub Pages

---

## PHASE 1 — Project Setup & Data

### T01 · File structure & shell
- Create full directory structure (`index.html`, `app.js`, `style.css`, `components/`, `data/`, `assets/`)
- `index.html` with Google Fonts CDN (Cormorant Garamond + Inter), viewport meta, root CSS vars
- Inline SVG icon set for: grid/category, filter, export, expand chevron, walkthrough arrow, missable warning ⚠
- Deploy to GitHub Pages (root of `main` branch)

### T02 · CSS design system
Extract from `design/option-1-dark-canvas.html` into `style.css`:
- All CSS custom properties (palette, typography, radius, spacing)
- Grain texture background
- Base reset and body styles
- Utility classes (badges, scrollbar styling)

### T03 · Data conversion — Excel → JSON
Convert all 15 sheets from `sources/ClairObscur_checklist_source.xlsx` to JSON files in `data/`.  
Each file follows the schema defined in `PROJECT.md`.

| File | Source Tab | Items | Special fields |
|---|---|---|---|
| `data/bosses-main.json` | Bosses (Main group) | ~30 | name, location, completed |
| `data/bosses-optional.json` | Bosses (Optional group) | 48 | name, location, missable, ign_url |
| `data/endless-tower.json` | Endless Tower | 33 trials | stage, trial, enemies, rewards, completed |
| `data/journals.json` | Expedition Journals | 49 | name, location, how_to_find, missable, completed |
| `data/haircuts.json` | Haircuts | 83 | name, character, location, how_to_find, missable, completed |
| `data/lost-gestrals.json` | Lost Gestrals | 9 | location, how_to_find, completed |
| `data/mimes.json` | Mimes | 15 | location, how_to_find, rewards, missable, completed |
| `data/monoco-skills.json` | Monoco Skills | 46 | name, description, enemy_location, completed |
| `data/music-records.json` | Music Records | 33 | name, location, how_to_find, missable, completed |
| `data/outfits.json` | Outfits | 77 | name, character, location, how_to_find, missable, completed |
| `data/paint-cages.json` | Paint Cages | 19 | location, how_to_find, rewards, completed |
| `data/petanks.json` | Petanks | 13 | location, how_to_find, rewards, completed |
| `data/pictos.json` | Pictos | 193 | name, effect, lumina_cost, location, how_to_find, missable, collected, lumina_unlocked |
| `data/quests.json` | Quests | 16 | name, location, how_to_complete, rewards, missable, ign_url, completed |
| `data/tint-upgrades.json` | Tint Upgrades | 33 | name, location, how_to_find, completed |
| `data/weapons.json` | Weapons | 108 | name, character, location, how_to_find, damage_type, max_damage, scaling, passives, completed |
| `data/categories.json` | — | 16 cats | id, name, icon, file, ign_url |

**IGN URLs to embed during conversion:**
- Optional bosses: per-item URLs from `CHECKLISTS.md`
- Quests: per-item URLs from `CHECKLISTS.md`
- All other categories: single category-level IGN URL applied to all items

---

## PHASE 2 — Core Architecture

### T04 · State manager (`app.js`)
```js
// State shape
{
  version: 1,
  completed: { "ob-001": true },          // regular checkbox
  pictos: { "p-042": "collected" | "lumina" }, // 3-state
  filters: { status: "all", act: null, missable: false },
  activeCategory: null                     // null = show all
}
```
- `loadState()` / `saveState()` via localStorage
- `toggle(id)` — cycles regular items between false/true
- `togglePicto(id)` — cycles none → collected → lumina → none
- `setFilter(key, value)`
- `setCategory(id)`

### T05 · Data loader
- `loadCategory(id)` — fetch JSON, cache in memory, merge with state
- `computeProgress(items)` — returns `{ done, total, pct }`
- `computeOverallProgress()` — aggregate across all categories

---

## PHASE 3 — Header & Navigation

### T06 · Header component (`components/Header.js`)
- App title + subtitle (Cormorant Garamond serif)
- Overall progress bar (gradient violet→gold)
- Overall % — 14px white
- Three icon buttons: Category, Filter, Export — always visible with gold borders

### T07 · Category overlay (`components/CategoryPage.js`)
- Full-screen slide-up panel triggered by Category button
- Lists all 16 categories with icon, name, and mini progress bar per category
- Tap category → closes overlay, scrolls main view to that section
- Shows "All" option at top to reset filter

### T08 · Filter panel (`components/FilterDropdown.js`)
- Slides down from header on Filter button tap
- Options:
  - **Status**: All / Done / Remaining
  - **Act**: All / Act 1 / Act 2 / Act 3
  - **Missable only**: toggle on/off
- Applying filter re-renders visible items

### T09 · Export (`app.js`)
- Serialize state to JSON
- Trigger download as `clairobscur-progress-[date].json`
- Import: file picker → validate → merge into state

---

## PHASE 4 — Category Sections

### T10 · Category section (`components/CategorySection.js`)
- Section header: decorative rules left/right, category title (21px Cormorant Garamond gold), X/Y count (13px white)
- Progress bar: gradient violet→gold, brushstroke sheen, % (13px white)
- Renders list of `ChecklistItem` components

### T11 · Checklist item — collapsed (`components/ChecklistItem.js`)
Collapsed row (44px min touch target):
- Checkbox/toggle (left)
- Item name (13px, `--text-1`)
- Location (11px, `--text-2`, truncated)
- Badges: ⚠ Missable (amber) and Act N (amber) — always visible, same color
- Walkthrough ↗ icon — gold border + gold color, taps open IGN in new tab, stops accordion toggle propagation
- Expand chevron ▾ (right)

### T12 · Checklist item — expanded (`components/ChecklistItem.js`)
Expanded card (accordion — only one open at a time):
- Purple border on card (`--violet`)
- Detail grid: Location · Act (or other metadata)
- Separator line
- Full description / How to Find text
- Rewards row (if applicable) — reward chips with colored dot (green if that item is also completed elsewhere)
- ⚠ Missable warning block (amber background, amber text)
- IGN Walkthrough button (gold border, subtle gold tint bg)

### T13 · 3-state Picto toggle
Two side-by-side circular buttons per Picto row:
- Left: ○ → ✓ green (Collected)
- Right: L → ★ blue (Lumina Unlocked)
- Right button only activates after left is active
- Tapping either cycles state; tapping collected off resets both

---

## PHASE 5 — Special Category Behaviours

### T14 · Character jump links (Haircuts, Outfits, Weapons, Monoco Skills)
- Sticky sub-header at top of section listing character names as tappable chips
- Tapping a chip scrolls to that character's sub-header anchor
- Characters: Gustave · Lune · Maelle · Sciel · Monoco · Verso · Esquie
- Weapons also has character grouping + same chips

### T15 · Character filter (Weapons, Monoco Skills)
- Filter tabs at top of section: All · Gustave/Verso · Lune · Maelle · Sciel · Monoco
- Tapping filters the visible items to that character only

### T16 · Endless Tower stage grouping
- Items grouped by Stage (1–11)
- Each stage row has a single checkbox (marks all 3 trials in that stage)
- Stage shows: "Stage N — Trial 1, Trial 2, Trial 3" in collapsed view
- Expanded: full enemy list + rewards for each trial

### T17 · Cross-reference badges (`components/CrossRef.js`)
- When a reward chip references an item tracked in another category (e.g. a Picto), show inline badge
- Badge shows item name + status dot: ✓ green (already collected) or ○ grey (not yet)
- Tapping badge scrolls to that item in its own section

---

## PHASE 6 — Polish & Mobile

### T18 · Mobile layout QA
- Test on 375px (iPhone SE) and 430px (iPhone Pro Max) widths
- All touch targets ≥ 44×44px
- No horizontal overflow
- Sticky header doesn't obscure content when scrolling to anchors (offset scroll)

### T19 · Scroll-to-category behavior
- When selecting a category from the overlay, smooth-scroll to the section heading
- Account for sticky header height in scroll offset

### T20 · Empty states & loading
- Show skeleton/placeholder while JSON loads
- "Nothing matches your filters" empty state with clear-filter button
- First-launch welcome note (dismissible)

### T21 · Performance
- Lazy-render categories not currently in viewport (IntersectionObserver)
- Avoid re-rendering all items on every state change — update only changed item's DOM

---

## PHASE 7 — Testing & Deploy

### T22 · Cross-browser test
- Safari iOS (primary target)
- Chrome Android
- Desktop Chrome (secondary)

### T23 · GitHub Pages deploy
- Confirm `index.html` at repo root
- Enable Pages from Settings → main branch / root
- Verify live URL works end-to-end

---

## TASK ORDER (recommended execution sequence)

```
T01 → T02 → T03          # Setup + all data ready before any UI
T04 → T05                 # State + data loading
T06 → T07 → T08 → T09   # Header + navigation
T10 → T11 → T12          # Core list rendering
T13                        # Picto 3-state (after T12)
T14 → T15                 # Character grouping + filter
T16                        # Endless Tower
T17                        # Cross-refs (after all items exist)
T18 → T19 → T20 → T21   # Polish
T22 → T23                 # QA + deploy
```

---

## UI RESOURCES REQUIRED

| Resource | Source | Notes |
|---|---|---|
| Cormorant Garamond (400, 600, italic) | Google Fonts CDN | Headings |
| Inter (300, 400, 500) | Google Fonts CDN | Body text |
| SVG icons | Inline / Lucide subset | grid, sliders, download, chevron, arrow-up-right, alert-triangle |
| Grain texture | CSS SVG filter (inline) | Already in design mockup |
| No game images needed | — | Pure CSS design |
