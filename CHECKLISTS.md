# Clair Obscur: Expedition 33 — Checklists Source Data

> Primary data source: `sources/ClairObscur_checklist_source.xlsx` (authoritative)  
> IGN walkthrough links: https://www.ign.com/wikis/clair-obscur-expedition-33  
> Platform achievements: 56 trophies (PS5) / 55 achievements (Xbox/Steam)

---

## IGN LINK STRATEGY

| Category | IGN Link Type | Notes |
|---|---|---|
| Bosses (Main) | Per-boss page | Each main boss has its own IGN page |
| Bosses (Optional) | Per-boss page | 48 bosses, each with individual IGN page |
| Endless Tower | Category page | Single page covers all 33 trials |
| Expedition Journals | Category page | `Expedition_Journal_Locations` — organized by h3 per journal |
| Haircuts | Category page | `Outfits_and_Haircuts_Guide:_All_Locations` |
| Lost Gestrals | Category page | `Sastro's_Lost_Gestral_Locations` |
| Mimes | Category page | `All_Mime_Locations` |
| Monoco Skills | Category page | No individual pages found |
| Music Records | Category page | No individual pages found |
| Outfits | Category page | `Outfits_and_Haircuts_Guide:_All_Locations` |
| Paint Cages | Category page | `Paint_Cage_Locations` |
| Petanks | Category page | No individual pages found |
| Pictos | Mixed | ~30 pictos have own page; rest → `All_Pictos_List_and_Effects` |
| Quests | Per-quest page | Each quest has its own IGN page |
| Tint Upgrades | Category page | `All_Tint_Shard_Locations` |
| Weapons | Category page | No individual pages found |

---

## CATEGORIES (from Excel source)

15 checklist tabs + 5 skill reference tabs (Lune, Maelle, Monoco, Sciel, Verso).

| # | Tab Name | Items | Columns | Special UX |
|---|---|---|---|---|
| 1 | Bosses | 116 total | Name, Location, Completed? | Two sections: Main Bosses / Optional Bosses |
| 2 | Endless Tower | 33 trials | Stage, Trial, Enemies, Rewards, Completed? | Grouped by Stage (11 stages × 3 trials) |
| 3 | Expedition Journals | 49 | Journal, Location, How to Find, Collected? | 1 missable (Fracture Survivor / Old Key) |
| 4 | Haircuts | 83 | Haircut, Location, How to Find, Collected? | Grouped by character; jump links at top |
| 5 | Lost Gestrals | 9 | Location, How to Find, Completed? | |
| 6 | Mimes | 15 | Location, How to Find, Rewards, Completed? | |
| 7 | Monoco Skills | 46 | Skill Name, Description, Enemy Location, Collected? | Skill checklist; filter by character at top (future-proof) |
| 8 | Music Records | 33 | Music Record, Location, How to Find, Collected? | 2 missable |
| 9 | Outfits | 77 | Outfit, Location, How to Find, Collected? | Grouped by character; jump links at top |
| 10 | Paint Cages | 19 | Location, How to Find, Rewards, Completed? | |
| 11 | Petanks | 13 | Location, How to Find, Rewards, Completed? | |
| 12 | Pictos | 193 | Picto, Effect, Lumina cost, Location, How to Find, Collected?, Lumina Unlocked? | **3-state toggle**: none / collected (green) / lumina (blue) |
| 13 | Quests | 16 | Quest, Location, How to Complete, Rewards, Completed? | Includes Nevron quests |
| 14 | Tint Upgrades | 33 | Item, Location, How to Find, Collected? | |
| 15 | Weapons | 108 | Weapon, Location, How to Find, Collected?, Damage Type, Max Damage, Scaling, Passives | Rich stats in expanded view |

**Reference only (no tracking):** Skill Damage Scaling — Lune, Maelle, Monoco, Sciel, Verso

---

## CHECKLIST COLUMN DETAILS

### 1. BOSSES

**Two sections within one category page:**

**Main Bosses** — story-required fights  
**Optional Bosses** — 48 bosses, each with individual IGN page

Columns: Name | Location | Completed?

**Optional Bosses — IGN links (complete list):**

| Boss Name | IGN Path |
|---|---|
| Chromatic Lancelier | /wikis/clair-obscur-expedition-33/Chromatic_Lancelier_(Spring_Meadows) |
| Bourgeon (Flying Waters) | /wikis/clair-obscur-expedition-33/Bourgeon_(Flying_Waters) |
| Chromatic Troubadour (Flying Waters) | /wikis/clair-obscur-expedition-33/Chromatic_Troubadour_(Flying_Waters) |
| Chromatic Abbest (Abbest Cave) | /wikis/clair-obscur-expedition-33/Chromatic_Abbest_(Abbest_Cave) |
| Chromatic Bruler (The Continent) | /wikis/clair-obscur-expedition-33/Chromatic_Bruler_(The_Continent) |
| Chromatic Hexga (Stone Wave Cliffs Cave) | /wikis/clair-obscur-expedition-33/Chromatic_Hexga_(Stone_Wave_Cliffs_Cave) |
| Glaise (Yellow Harvest) | /wikis/clair-obscur-expedition-33/Glaise_(Yellow_Harvest) |
| Chromatic Luster (Forgotten Battlefield) | /wikis/clair-obscur-expedition-33/Chromatic_Luster_(Forgotten_Battlefield) |
| Grosse Tete (The Continent) | /wikis/clair-obscur-expedition-33/Grosse_Tete_(The_Continent) |
| Chromatic Danseuse (Old Lumiere) | /wikis/clair-obscur-expedition-33/Chromatic_Danseuse_(Old_Lumiere) |
| Chromatic Boucheclier (Isle of the Eyes) | /wikis/clair-obscur-expedition-33/Chromatic_Boucheclier_(Isle_of_the_Eyes) |
| Chromatic Goblu (The Continent) | /wikis/clair-obscur-expedition-33/Chromatic_Goblu_(The_Continent) |
| Chromatic Catapult Sakapatate (Dark Gestral Arena) | /wikis/clair-obscur-expedition-33/Chromatic_Catapult_Sakapatate_(Dark_Gestral_Arena) |
| Chromatic Ranger Sakapatate (Dark Gestral Arena) | /wikis/clair-obscur-expedition-33/Chromatic_Ranger_Sakapatate_(Dark_Gestral_Arena) |
| Chromatic Robust Sakapatate (Dark Gestral Arena) | /wikis/clair-obscur-expedition-33/Chromatic_Robust_Sakapatate_(Dark_Gestral_Arena) |
| Golgra (Dark Gestral Arena) | /wikis/clair-obscur-expedition-33/Golgra_(Dark_Gestral_Arena) |
| Chromatic Portier (The Continent) | /wikis/clair-obscur-expedition-33/Chromatic_Portier_(The_Continent) |
| Chromatic Benisseur (The Continent) | /wikis/clair-obscur-expedition-33/Chromatic_Benisseur_(The_Continent) |
| Thunder Eveque (The Continent) | /wikis/clair-obscur-expedition-33/Thunder_Eveque_(The_Continent) |
| Serpenphare (The Continent) | /wikis/clair-obscur-expedition-33/Serpenphare_(The_Continent) |
| Chromatic Glaise (Sky Island) | /wikis/clair-obscur-expedition-33/Chromatic_Glaise_(Sky_Island) |
| Painted Love (Endless Tower) | /wikis/clair-obscur-expedition-33/Painted_Love_(Endless_Tower) |
| Chromatic Gold Chevaliere (Crimson Forest) | /wikis/clair-obscur-expedition-33/Chromatic_Gold_Chevaliere_(Crimson_Forest) |
| Chromatic Clair Obscur (The Monolith) | /wikis/clair-obscur-expedition-33/Chromatic_Clair_Obscur_(The_Monolith) |
| Chromatic Cruler (Endless Night Sanctuary) | /wikis/clair-obscur-expedition-33/Chromatic_Cruler_(Endless_Night_Sanctuary) |
| Chromatic Glissando (Sirene's Dress) | /wikis/clair-obscur-expedition-33/Chromatic_Glissando_(Sirene%27s_Dress) |
| Flame Eveque (Flying Manor) | /wikis/clair-obscur-expedition-33/Flame_Eveque_(Flying_Manor) |
| Clea (Flying Manor) | /wikis/clair-obscur-expedition-33/Clea_(Flying_Manor) |
| Chromatic Braseleur (The Reacher) | /wikis/clair-obscur-expedition-33/Chromatic_Braseleur_(The_Reacher) |
| Alicia (The Reacher) | /wikis/clair-obscur-expedition-33/Alicia_(The_Reacher) |
| Chromatic Creation (Renoir's Drafts) | /wikis/clair-obscur-expedition-33/Chromatic_Creation_(Renoir%27s_Drafts) |
| Chromatic Echassier (Lumiere) | /wikis/clair-obscur-expedition-33/Chromatic_Echassier_(Lumiere) |
| *(remaining 16 bosses — IGN list has 48 total; full extract in data/optional-bosses.json)* | |

> Full 48-boss IGN link list to be stored in `data/bosses.json` during data preparation phase.

---

### 2. ENDLESS TOWER

Columns: Stage | Trial | Enemies | Rewards | Completed?  
Structure: 11 stages, 3 trials each = 33 total trials  
Checkbox per **stage** (marks all 3 trials in that stage as done)  
IGN: `https://www.ign.com/wikis/clair-obscur-expedition-33/Endless_Tower`

---

### 3. EXPEDITION JOURNALS

Columns: Journal | Location | How to Find | Collected?  
Count: 49 journals  
**1 missable**: "Fracture Survivor" in Old Lumière — requires Old Key obtained by trading Festival Token in Prologue  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/Expedition_Journal_Locations`

---

### 4. HAIRCUTS

Columns: Haircut | Location | How to Find | Collected?  
Count: 83 haircuts, grouped by character  
Characters: Gustave, Lune, Maelle, Sciel, Monoco, Verso, Esquie  
Jump links at top of section to scroll to each character's sub-list  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/Outfits_and_Haircuts_Guide:_All_Locations`

---

### 5. LOST GESTRALS

Columns: Location | How to Find | Completed?  
Count: 9  
Finding first 4 unlocks Paint Break ability (required for some Paint Cages)  
IGN page: `https://www.ign.com/wikis/clair-obscur-expedition-33/Sastro%27s_Lost_Gestral_Locations`

---

### 6. MIMES

Columns: Location | How to Find | Rewards | Completed?  
Count: 15  
**First Mime (Prologue) is missable** — required for Music Record "Lumiere" and "A Peculiar Encounter" achievement  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/All_Mime_Locations`

---

### 7. MONOCO SKILLS

Columns: Skill Name | Skill Description | Enemy Location | Collected?  
Count: 46 skills  
Monoco acquires skills by defeating specific enemy types. Each skill requires finding and defeating its source enemy.  
Collapsed view: Skill Name + Collected?  
Expanded view: Full skill description + Enemy Location + all stats  
Character filter at top (currently only Monoco; structure allows adding other characters later)  
IGN: No dedicated page found — use `https://www.ign.com/wikis/clair-obscur-expedition-33/Monoco` as fallback

---

### 8. MUSIC RECORDS

Columns: Music Record | Location | How to Find | Collected?  
Count: 33  
**2 missable:**
- "Lumiere" — defeat Prologue Mime (also obtainable in Act 2 as fallback)
- "Lettre à Maelle" — complete optional camp scene before leaving for Act 2

IGN: No dedicated music records list page found on IGN. Use PowerPyx as external reference.

---

### 9. OUTFITS

Columns: Outfit | Location | How to Find | Collected?  
Count: 77 outfits, grouped by character  
Characters: Gustave, Lune, Maelle, Sciel, Monoco, Verso, Esquie  
Jump links at top of section to scroll to each character's sub-list  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/Outfits_and_Haircuts_Guide:_All_Locations`

---

### 10. PAINT CAGES

Columns: Location | How to Find | Rewards | Completed?  
Count: 19  
Each cage requires shooting 3 nearby locks to open  
Some require Paint Break ability (get by finding 4 Lost Gestrals first)  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/Paint_Cage_Locations`

---

### 11. PETANKS

Columns: Location | How to Find | Rewards | Completed?  
Count: 13  
Petanks are special mini-boss encounters you must chase and corner  
IGN: No dedicated page found; each Petank may appear in area walkthrough pages

---

### 12. PICTOS

Columns: Picto | Effect | Lumina cost | Location | How to Find | Collected? | Lumina Unlocked?  
Count: 193 base game  
**3-state toggle per item:**
- ○ Not collected (default)
- ● Collected — green
- ★ Lumina Unlocked — blue

**2 missable:**
- "Exposing Attack" — purchase from merchant Noco (area-limited)
- "Auto Powerful" — complete Chalier Nevron quest and agree to end its life

IGN: ~30 pictos have individual pages at `https://www.ign.com/wikis/clair-obscur-expedition-33/[PictoName]`  
Remaining pictos → `https://www.ign.com/wikis/clair-obscur-expedition-33/All_Pictos_List_and_Effects`

---

### 13. QUESTS

Columns: Quest | Location | How to Complete | Rewards | Completed?  
Count: 16 side quests (includes Nevron quests)  
IGN per-quest links (from Side Quests page):

| Quest Name | IGN Path |
|---|---|
| A Uniform for Richard's Son | /wikis/clair-obscur-expedition-33/Prologue:_A_Uniform_for_Richard%27s_Son |
| Jar's Light Quest | /wikis/clair-obscur-expedition-33/Jar%27s_Light_Quest_-_Where_to_Find_Light |
| Demineur Quest | /wikis/clair-obscur-expedition-33/Demineur_Quest_-_Where_to_Find_a_Mine |
| Karatom Quest | /wikis/clair-obscur-expedition-33/Karatom_Quest_-_Where_to_Find_Blue_Mushrooms |
| The Small Bourgeon Quest | /wikis/clair-obscur-expedition-33/The_Small_Bourgeon_Quest_-_Where_to_Find_Bourgeon_Skin |
| Help Alexsoundro | /wikis/clair-obscur-expedition-33/Help_Alexsoundro |
| Ono-Puncho Challenge | /wikis/clair-obscur-expedition-33/How_to_Beat_the_Ono-Puncho_Challenge |
| Hidden Gestral Arena | /wikis/clair-obscur-expedition-33/Hidden_Gestral_Arena |
| Sastro's Lost Gestrals | /wikis/clair-obscur-expedition-33/Sastro%27s_Lost_Gestral_Locations |
| Gestral Beach Parkour | /wikis/clair-obscur-expedition-33/Gestral_Beach_-_Parkour_Challenge |
| Hexga Quest | /wikis/clair-obscur-expedition-33/Hexga_Quest_-_Where_to_Find_Glowing_Rock_Crystals |
| *(remaining quests — full list in data/quests.json)* | |

> Full quest IGN link list to be stored in `data/quests.json` during data preparation phase.

---

### 14. TINT UPGRADES

Columns: Item | Location | How to Find | Collected?  
Count: 33 Healing Tint Shards  
IGN category page: `https://www.ign.com/wikis/clair-obscur-expedition-33/All_Tint_Shard_Locations`

---

### 15. WEAPONS

Columns: Weapon | Location | How to Find | Collected? | Damage Type | Max Damage | Scaling | Passives  
Count: 108 weapons (shared across Gustave/Verso and other characters)  
Collapsed view: Weapon Name + Location + Collected? + external link icon  
Expanded view: All stats (Damage Type, Max Damage, Scaling stat, multi-level Passives description)  
IGN: `https://www.ign.com/wikis/clair-obscur-expedition-33/How_to_Upgrade_Your_Weapons` (general; no per-weapon pages found)

---

## CROSS-CHECKLIST RELATIONSHIPS

Items where one category references another — displayed as inline badges.

| Source | References | Target |
|---|---|---|
| Mimes (Prologue Mime) | Music Record: Lumiere | Music Records |
| Mimes (Prologue Mime) | Achievement: A Peculiar Encounter | Trophies |
| Quests (Chalier Nevron) | Picto: Auto Powerful | Pictos |
| Quests (Hexga Nevron) | Picto: Auto Shell | Pictos |
| Quests (Troubadour Nevron) | Picto: Healing Parry | Pictos |
| Quests (Portier Nevron) | Picto: Protecting Heal | Pictos |
| Quests (Benisseur Nevron) | Picto: Recovery | Pictos |
| Optional Bosses (Clea) | Picto: Clea's Life | Pictos |
| Optional Bosses (Grosse Tete) | Picto: Warming Up | Pictos |
| Optional Bosses (Sprong) | Picto: Cheater | Pictos |
| Optional Bosses (Serpenphare) | Picto: Energy Master | Pictos |
| Lost Gestrals (first 4) | Unlocks Paint Break → required for Paint Cages #14 and #15 | Paint Cages |
| Expedition Journal #7 | Requires Old Key (trade Festival Token in Prologue) | Quests |

---

## SOURCES

**Primary:**
- `sources/ClairObscur_checklist_source.xlsx` — authoritative checklist data for all 15 categories

**IGN Walkthrough (per-item links):**
- Optional Bosses: https://www.ign.com/wikis/clair-obscur-expedition-33/Optional_Bosses
- Side Quests: https://www.ign.com/wikis/clair-obscur-expedition-33/Side_Quests

**IGN Category Pages:**
- Outfits & Haircuts: https://www.ign.com/wikis/clair-obscur-expedition-33/Outfits_and_Haircuts_Guide:_All_Locations
- Expedition Journals: https://www.ign.com/wikis/clair-obscur-expedition-33/Expedition_Journal_Locations
- Paint Cages: https://www.ign.com/wikis/clair-obscur-expedition-33/Paint_Cage_Locations
- All Pictos: https://www.ign.com/wikis/clair-obscur-expedition-33/All_Pictos_List_and_Effects
- Tint Upgrades: https://www.ign.com/wikis/clair-obscur-expedition-33/All_Tint_Shard_Locations
- Mimes: https://www.ign.com/wikis/clair-obscur-expedition-33/All_Mime_Locations
- Lost Gestrals: https://www.ign.com/wikis/clair-obscur-expedition-33/Sastro%27s_Lost_Gestral_Locations

**Supplementary:**
- PowerPyx Trophy Guide: https://www.powerpyx.com/clair-obscur-expedition-33-trophy-guide-roadmap/
- Fextralife Wiki: https://expedition33.wiki.fextralife.com/
