# Clair Obscur Tracker — Dev Rules

## ⚠ CRITICAL: Never break localStorage compatibility

All user progress (checked items, picto states) is saved in `localStorage` under the key `co33-tracker-v1`.

**State shape (must stay backward-compatible):**
```js
{
  version: 1,
  completed: { "item-id": true },          // regular checkboxes
  pictos:    { "item-id": "collected" | "lumina" }, // 3-state picto toggle
  filters:   { status: "all", missable: "all" }
}
```

**Rules:**
- Never rename or change the `localStorage` key `co33-tracker-v1`
- Never change existing item `id` values in any `data/*.json` file — these are the keys users have saved
- If new fields are added to state, always provide a default so old saved state still works (`{ ...defaultState(), ...JSON.parse(raw) }`)
- If a data schema change requires new IDs, write a migration in `loadState()` that converts old keys to new ones before saving

**Why:** The app is public on GitHub Pages. Real users are already marking items. Any breaking change silently wipes their progress with no warning or recovery path.

## Stack
- Vanilla JS (ES modules), no build step
- CSS custom properties, no framework
- Static JSON data files in `data/`
- GitHub Pages hosting (push to `main` → live)

## No hover effects
App is used on Android (Google Pixel). Never add `:hover` CSS rules — all visual states must be always-visible without mouse interaction.

## Local dev
```bash
python3 -m http.server 8765
# open http://localhost:8765
```
