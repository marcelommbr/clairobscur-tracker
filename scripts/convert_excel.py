"""
Convert ClairObscur_checklist_source.xlsx to individual JSON files in data/
Run from project root: python3 scripts/convert_excel.py
"""
import json, re, os
import pandas as pd

SRC = "sources/ClairObscur_checklist_source.xlsx"
OUT = "data"
BASE_IGN = "https://www.ign.com/wikis/clair-obscur-expedition-33"

IGN_CATEGORY_URLS = {
    "bosses-optional":  f"{BASE_IGN}/Optional_Bosses",
    "bosses-main":      f"{BASE_IGN}/Walkthrough",
    "endless-tower":    f"{BASE_IGN}/Endless_Tower",
    "journals":         f"{BASE_IGN}/Expedition_Journal_Locations",
    "haircuts":         f"{BASE_IGN}/Outfits_and_Haircuts_Guide:_All_Locations",
    "outfits":          f"{BASE_IGN}/Outfits_and_Haircuts_Guide:_All_Locations",
    "lost-gestrals":    f"{BASE_IGN}/Sastro%27s_Lost_Gestral_Locations",
    "mimes":            f"{BASE_IGN}/All_Mime_Locations",
    "monoco-skills":    f"{BASE_IGN}/Monoco",
    "music-records":    f"{BASE_IGN}/All_Pictos_List_and_Effects",
    "paint-cages":      f"{BASE_IGN}/Paint_Cage_Locations",
    "petanks":          f"{BASE_IGN}/Optional_Bosses",
    "pictos":           f"{BASE_IGN}/All_Pictos_List_and_Effects",
    "quests":           f"{BASE_IGN}/Side_Quests",
    "tint-upgrades":    f"{BASE_IGN}/All_Tint_Shard_Locations",
    "weapons":          f"{BASE_IGN}/How_to_Upgrade_Your_Weapons",
}

# Per-item IGN overrides for optional bosses (from CHECKLISTS.md research)
BOSS_IGN = {
    "Chromatic Lancelier": f"{BASE_IGN}/Chromatic_Lancelier_(Spring_Meadows)",
    "Bourgeon (Flying Waters)": f"{BASE_IGN}/Bourgeon_(Flying_Waters)",
    "Chromatic Troubadour (Flying Waters)": f"{BASE_IGN}/Chromatic_Troubadour_(Flying_Waters)",
    "Chromatic Abbest (Abbest Cave)": f"{BASE_IGN}/Chromatic_Abbest_(Abbest_Cave)",
    "Chromatic Bruler (The Continent)": f"{BASE_IGN}/Chromatic_Bruler_(The_Continent)",
    "Chromatic Hexga (Stone Wave Cliffs Cave)": f"{BASE_IGN}/Chromatic_Hexga_(Stone_Wave_Cliffs_Cave)",
    "Glaise (Yellow Harvest)": f"{BASE_IGN}/Glaise_(Yellow_Harvest)",
    "Chromatic Luster (Forgotten Battlefield)": f"{BASE_IGN}/Chromatic_Luster_(Forgotten_Battlefield)",
    "Grosse Tete (The Continent)": f"{BASE_IGN}/Grosse_Tete_(The_Continent)",
    "Chromatic Danseuse (Old Lumiere)": f"{BASE_IGN}/Chromatic_Danseuse_(Old_Lumiere)",
    "Chromatic Boucheclier (Isle of the Eyes)": f"{BASE_IGN}/Chromatic_Boucheclier_(Isle_of_the_Eyes)",
    "Chromatic Goblu (The Continent)": f"{BASE_IGN}/Chromatic_Goblu_(The_Continent)",
    "Chromatic Catapult Sakapatate (Dark Gestral Arena)": f"{BASE_IGN}/Chromatic_Catapult_Sakapatate_(Dark_Gestral_Arena)",
    "Chromatic Ranger Sakapatate (Dark Gestral Arena)": f"{BASE_IGN}/Chromatic_Ranger_Sakapatate_(Dark_Gestral_Arena)",
    "Chromatic Robust Sakapatate (Dark Gestral Arena)": f"{BASE_IGN}/Chromatic_Robust_Sakapatate_(Dark_Gestral_Arena)",
    "Golgra (Dark Gestral Arena)": f"{BASE_IGN}/Golgra_(Dark_Gestral_Arena)",
    "Chromatic Portier (The Continent)": f"{BASE_IGN}/Chromatic_Portier_(The_Continent)",
    "Chromatic Benisseur (The Continent)": f"{BASE_IGN}/Chromatic_Benisseur_(The_Continent)",
    "Thunder Eveque (The Continent)": f"{BASE_IGN}/Thunder_Eveque_(The_Continent)",
    "Serpenphare (The Continent)": f"{BASE_IGN}/Serpenphare_(The_Continent)",
    "Chromatic Glaise (Sky Island)": f"{BASE_IGN}/Chromatic_Glaise_(Sky_Island)",
    "Painted Love (Endless Tower)": f"{BASE_IGN}/Painted_Love_(Endless_Tower)",
    "Chromatic Gold Chevaliere (Crimson Forest)": f"{BASE_IGN}/Chromatic_Gold_Chevaliere_(Crimson_Forest)",
    "Chromatic Clair Obscur (The Monolith)": f"{BASE_IGN}/Chromatic_Clair_Obscur_(The_Monolith)",
    "Chromatic Cruler (Endless Night Sanctuary)": f"{BASE_IGN}/Chromatic_Cruler_(Endless_Night_Sanctuary)",
    "Chromatic Glissando (Sirene's Dress)": f"{BASE_IGN}/Chromatic_Glissando_(Sirene%27s_Dress)",
    "Flame Eveque (Flying Manor)": f"{BASE_IGN}/Flame_Eveque_(Flying_Manor)",
    "Clea (Flying Manor)": f"{BASE_IGN}/Clea_(Flying_Manor)",
    "Chromatic Braseleur (The Reacher)": f"{BASE_IGN}/Chromatic_Braseleur_(The_Reacher)",
    "Alicia (The Reacher)": f"{BASE_IGN}/Alicia_(The_Reacher)",
    "Chromatic Creation (Renoir's Drafts)": f"{BASE_IGN}/Chromatic_Creation_(Renoir%27s_Drafts)",
    "Chromatic Echassier (Lumiere)": f"{BASE_IGN}/Chromatic_Echassier_(Lumiere)",
}

# Per-item IGN overrides for quests
QUEST_IGN = {
    "A Uniform for Richard's Son": f"{BASE_IGN}/Prologue:_A_Uniform_for_Richard%27s_Son",
    "Blanche": f"{BASE_IGN}/All_Nevron_Quests",
    "Jar": f"{BASE_IGN}/Jar%27s_Light_Quest_-_Where_to_Find_Light",
    "Demineur": f"{BASE_IGN}/Demineur_Quest_-_Where_to_Find_a_Mine",
    "Karatom": f"{BASE_IGN}/Karatom_Quest_-_Where_to_Find_Blue_Mushrooms",
    "Bourgeon": f"{BASE_IGN}/The_Small_Bourgeon_Quest_-_Where_to_Find_Bourgeon_Skin",
    "Help Alexsoundro": f"{BASE_IGN}/Help_Alexsoundro",
    "Hexga": f"{BASE_IGN}/Hexga_Quest_-_Where_to_Find_Glowing_Rock_Crystals",
    "Troubadour": f"{BASE_IGN}/All_Nevron_Quests",
    "Portier": f"{BASE_IGN}/All_Nevron_Quests",
    "Benisseur": f"{BASE_IGN}/All_Nevron_Quests",
    "Danseuse Teacher": f"{BASE_IGN}/All_Nevron_Quests",
    "Chalier": f"{BASE_IGN}/All_Nevron_Quests",
    "Grandis": f"{BASE_IGN}/All_Nevron_Quests",
}

def extract_act(name_str, location_str, how_str=""):
    """Return act number if item is explicitly restricted to a specific act.
    Only matches parenthetical act markers in location/name like '(Act III)'
    to avoid false positives from narrative text like 'before entering Act II'.
    """
    import re
    # Only check location and name — not how_to_find (too many false positives)
    structured = f"{name_str} {location_str}"
    # Must appear in parentheses: (Act III), (Act 3), (Act III, Missable), etc.
    m = re.search(r'\(\s*act\s*(iii|3)\b', structured, re.IGNORECASE)
    if m: return 3
    m = re.search(r'\(\s*act\s*(ii|2)\b', structured, re.IGNORECASE)
    if m: return 2
    m = re.search(r'\(\s*act\s*(i|1)\b', structured, re.IGNORECASE)
    if m: return 1
    return None

def slug(text, prefix, idx):
    return f"{prefix}-{idx:03d}"

def is_missable(name_str, location_str=""):
    """Check name AND location for missable indicator."""
    combined = f"{name_str} {location_str}".lower()
    return "missable" in combined

def clean_name(val):
    """Strip text, also remove trailing (Missable) / (missable) from names."""
    if pd.isna(val):
        return ""
    s = str(val).strip().replace("\n", " ").replace("\\n", " ")
    # Remove "(Missable)" variants from display name
    import re
    s = re.sub(r'\s*\(missable\)', '', s, flags=re.IGNORECASE).strip()
    return s

def clean(val):
    if pd.isna(val):
        return ""
    return str(val).strip().replace("\n", " ").replace("\\n", " ")

# ── BOSS REWARDS LOOKUP ───────────────────────────────────────
# Source: CHECKLISTS.md research + IGN/PowerPyx guides
BOSS_REWARDS = {
    # Named/Secret bosses
    "Alicia":           "Painted Me Haircut, Lithum Weapon, Resplendent Chroma Catalysts",
    "Clea":             "Clea's Life Pictos, Perfect Chroma Catalyst, Grandiose Chroma Catalysts",
    "Simon":            "Simoso Weapon, Perfect Chroma Catalysts, 50× Colour of Lumina",
    "Grosse Tete":      "Warming Up Pictos, Resplendent Chroma Catalyst",
    "Sprong":           "Cheater Pictos, Grandiose Chroma Catalysts",
    "Serpenphare":      "Energy Master Pictos, Perfect Chroma Catalyst, Grandiose Chroma Catalyst",
    "Golgra":           "EXP, rare items",
    "Painted Love":     "Resplendent Chroma Catalysts, Colour of Lumina",
    # Chromatic bosses (general pattern)
    "_chromatic":       "Resplendent Chroma Catalyst, Colour of Lumina",
    # Gestral Arena bosses
    "Chromatic Catapult Sakapatate": "Resplendent Chroma Catalyst, Colour of Lumina",
    "Chromatic Ranger Sakapatate":   "Resplendent Chroma Catalyst, Colour of Lumina",
    "Chromatic Robust Sakapatate":   "Resplendent Chroma Catalyst, Colour of Lumina",
    # World bosses / Elemental Eveques
    "Thunder Eveque":   "Grandiose Chroma Catalysts, Colour of Lumina",
    "Flame Eveque":     "Grandiose Chroma Catalysts, Colour of Lumina",
    # Other notable
    "Glaise":           "Resplendent Chroma Catalyst, Colour of Lumina",
    "Grown Bourgeon":   "Colour of Lumina, Chroma Catalysts",
}

def get_boss_rewards(name):
    """Return rewards string for a boss by name."""
    # Exact match first
    if name in BOSS_REWARDS:
        return BOSS_REWARDS[name]
    # Partial match for named bosses (e.g. "Grosse Tete (The Continent)")
    for key, val in BOSS_REWARDS.items():
        if key.startswith('_'):
            continue
        if key.lower() in name.lower():
            return val
    # Chromatic bosses fallback
    if "chromatic" in name.lower():
        return BOSS_REWARDS["_chromatic"]
    # Generic fallback for all bosses
    return "EXP, Chroma Catalysts, Colour of Lumina"

def save(filename, data):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ {filename} ({len(data['items'])} items)")

def read_sheet(sheet, header_row=None):
    """Read a sheet, auto-detecting the header row if not specified."""
    df = pd.read_excel(SRC, sheet_name=sheet, header=None)
    if header_row is None:
        # Find first row where col 0 or 1 has actual text (not NaN)
        for i, row in df.iterrows():
            vals = [str(v).strip() for v in row if not pd.isna(v) and str(v).strip()]
            if len(vals) >= 2 and i > 0:
                header_row = i
                break
    df.columns = range(len(df.columns))
    return df, header_row

# ── BOSSES ──────────────────────────────────────────────────────────────────
def convert_bosses():
    df = pd.read_excel(SRC, sheet_name="Bosses", header=None)
    # Main bosses in cols 1,2,3 | Optional bosses in cols 5,6,7
    main_items, opt_items = [], []

    for i, row in df.iterrows():
        if i < 2: continue  # skip header rows

        # Main boss: col1=name, col2=location, col3=completed
        name_m = clean_name(row[1])
        loc_m  = clean(row[2])
        if name_m and name_m not in ("Main Bosses", "Location", "Completed?"):
            main_items.append({
                "id": slug("bm", "bm", len(main_items)),
                "name": name_m,
                "location": loc_m,
                "rewards": get_boss_rewards(name_m),
                "missable": is_missable(name_m, loc_m),
                "act": extract_act(name_m, loc_m),
                "ign_url": IGN_CATEGORY_URLS["bosses-main"],
                "completed": False,
            })

        # Optional boss: col5=name, col6=location, col7=completed
        name_o = clean_name(row[5])
        loc_o  = clean(row[6])
        if name_o and name_o not in ("Optional Bosses", "Location", "Completed?"):
            full_name = f"{name_o} ({loc_o})" if loc_o else name_o
            ign = BOSS_IGN.get(full_name) or BOSS_IGN.get(name_o) or IGN_CATEGORY_URLS["bosses-optional"]
            # Mark known missable secret bosses
            missable_bosses = {"Alicia", "Clea", "Simon"}
            opt_items.append({
                "id": slug("bo", "bo", len(opt_items)),
                "name": name_o,
                "location": loc_o,
                "rewards": get_boss_rewards(name_o),
                "missable": name_o in missable_bosses or is_missable(name_o, loc_o),
                "act": extract_act(name_o, loc_o),
                "ign_url": ign,
                "completed": False,
            })

    save("bosses-main.json", {"id": "bosses-main", "name": "Main Bosses", "ign_url": IGN_CATEGORY_URLS["bosses-main"], "items": main_items})
    save("bosses-optional.json", {"id": "bosses-optional", "name": "Optional Bosses", "ign_url": IGN_CATEGORY_URLS["bosses-optional"], "items": opt_items})

# ── ENDLESS TOWER ────────────────────────────────────────────────────────────
def convert_endless_tower():
    df = pd.read_excel(SRC, sheet_name="Endless Tower", header=None)
    items = []
    current_stage = None
    for i, row in df.iterrows():
        if i < 2: continue
        stage_val = clean(row[0])
        trial_val = clean(row[1])
        enemies   = clean(row[2])
        rewards   = clean(row[8])
        completed = str(row[15]).strip().lower() == "true" if not pd.isna(row[15]) else False

        if stage_val and stage_val.isdigit():
            current_stage = int(stage_val)
        if trial_val and trial_val.isdigit() and current_stage is not None:
            items.append({
                "id": f"et-s{current_stage:02d}-t{int(trial_val)}",
                "stage": current_stage,
                "trial": int(trial_val),
                "enemies": enemies,
                "rewards": rewards,
                "completed": completed,
            })

    save("endless-tower.json", {"id": "endless-tower", "name": "Endless Tower", "ign_url": IGN_CATEGORY_URLS["endless-tower"], "items": items})

# ── EXPEDITION JOURNALS ──────────────────────────────────────────────────────
def convert_journals():
    df = pd.read_excel(SRC, sheet_name="Expedition Journals", header=None)
    items = []
    current_name = None
    current_location = None
    current_how = []
    current_completed = False

    def flush():
        nonlocal current_name, current_location, current_how, current_completed
        if current_name:
            missable = current_name == "Fracture Survivor"
            items.append({
                "id": slug("j", "j", len(items)),
                "name": current_name,
                "location": current_location or "",
                "how_to_find": " ".join(current_how).strip(),
                "missable": missable,
                "act": extract_act(current_name, current_location or "", " ".join(current_how)),
                "ign_url": IGN_CATEGORY_URLS["journals"],
                "completed": current_completed,
            })
        current_name = None; current_location = None; current_how = []; current_completed = False

    for i, row in df.iterrows():
        if i < 2: continue
        name = clean(row[0])
        loc  = clean(row[2])
        how  = clean(row[4])
        comp = str(row[13]).strip().lower() == "true" if not pd.isna(row[13]) else False

        if name:
            flush()
            current_name = name
            current_location = loc
            current_how = [how] if how else []
            current_completed = comp
        elif how:
            current_how.append(how)

    flush()
    save("journals.json", {"id": "journals", "name": "Expedition Journals", "ign_url": IGN_CATEGORY_URLS["journals"], "items": items})

# ── HAIRCUTS ─────────────────────────────────────────────────────────────────
def convert_haircuts():
    df = pd.read_excel(SRC, sheet_name="Haircuts", header=None)
    items = []
    current_character = None

    for i, row in df.iterrows():
        if i < 2: continue
        name = clean(row[0])
        loc  = clean(row[2])
        how  = clean(row[4])
        comp = str(row[10]).strip().lower() == "true" if not pd.isna(row[10]) else False

        # Character header rows have name but no location and no how_to_find
        if name and not loc and not how and name not in ("Haircut", "Location", "How to Find"):
            current_character = name
            continue

        if name and name not in ("Haircut", "Location", "How to Find") and current_character:
            display_name = clean_name(name)
            items.append({
                "id": slug("h", "h", len(items)),
                "name": display_name,
                "character": current_character,
                "location": loc,
                "how_to_find": how,
                "missable": is_missable(name, loc),
                "act": extract_act(name, loc, how),
                "ign_url": IGN_CATEGORY_URLS["haircuts"],
                "completed": comp,
            })

    save("haircuts.json", {"id": "haircuts", "name": "Haircuts", "ign_url": IGN_CATEGORY_URLS["haircuts"], "items": items})

# ── LOST GESTRALS ─────────────────────────────────────────────────────────────
def convert_lost_gestrals():
    df = pd.read_excel(SRC, sheet_name="Lost Gestrals", header=None)
    items = []
    for i, row in df.iterrows():
        if i < 2: continue
        loc  = clean(row[0])
        how  = clean(row[2])
        comp = str(row[6]).strip().lower() == "true" if not pd.isna(row[6]) else False
        if loc and loc not in ("Location", "How to Find"):
            items.append({
                "id": slug("lg", "lg", len(items)),
                "location": loc,
                "how_to_find": how,
                "missable": False,
                "ign_url": IGN_CATEGORY_URLS["lost-gestrals"],
                "completed": comp,
            })

    save("lost-gestrals.json", {"id": "lost-gestrals", "name": "Lost Gestrals", "ign_url": IGN_CATEGORY_URLS["lost-gestrals"], "items": items})

# ── MIMES ─────────────────────────────────────────────────────────────────────
def convert_mimes():
    df = pd.read_excel(SRC, sheet_name="Mimes", header=None)
    items = []
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        loc     = clean(row[0])
        how     = clean(row[2])
        rewards = clean(row[11])
        comp    = str(row[14]).strip().lower() == "true" if not pd.isna(row[14]) else False

        if loc and loc not in ("Location", "How to Find"):
            flush()
            current = {
                "id": slug("m", "m", len(items)),
                "location": loc,
                "how_to_find": how,
                "rewards": rewards,
                "missable": is_missable(loc),
                "ign_url": IGN_CATEGORY_URLS["mimes"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()
        elif current and rewards:
            current["rewards"] = (current["rewards"] + " " + rewards).strip()

    flush()
    save("mimes.json", {"id": "mimes", "name": "Mimes", "ign_url": IGN_CATEGORY_URLS["mimes"], "items": items})

# ── MONOCO SKILLS ──────────────────────────────────────────────────────────────
def convert_monoco_skills():
    df = pd.read_excel(SRC, sheet_name="Monoco Skills", header=None)
    items = []
    for i, row in df.iterrows():
        if i < 2: continue
        name  = clean(row[0])
        desc  = clean(row[1])
        loc   = clean(row[2])
        comp_raw = row[3]
        comp  = False if pd.isna(comp_raw) else (str(comp_raw).strip() not in ("0", "False", "false", ""))
        if name and name not in ("Skill Name", "Skill description", "Enemy Location"):
            items.append({
                "id": slug("ms", "ms", len(items)),
                "name": name,
                "character": "Monoco",
                "description": desc,
                "enemy_location": loc,
                "missable": False,
                "ign_url": IGN_CATEGORY_URLS["monoco-skills"],
                "completed": comp,
            })

    save("monoco-skills.json", {"id": "monoco-skills", "name": "Monoco Skills", "ign_url": IGN_CATEGORY_URLS["monoco-skills"], "items": items})

# ── MUSIC RECORDS ──────────────────────────────────────────────────────────────
MISSABLE_RECORDS = {"Lumiere", "Lettre à Maelle", "Lettre a Maelle"}

def convert_music_records():
    df = pd.read_excel(SRC, sheet_name="Music Records", header=None)
    items = []
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        name = clean(row[0])
        loc  = clean(row[2])
        how  = clean(row[4])
        comp = str(row[13]).strip().lower() == "true" if not pd.isna(row[13]) else False

        if name and name not in ("Music Record", "Location", "How to Find"):
            flush()
            display_name = clean_name(name)
            current = {
                "id": slug("mr", "mr", len(items)),
                "name": display_name,
                "location": loc,
                "how_to_find": how,
                "missable": is_missable(name, loc) or display_name in MISSABLE_RECORDS,
                "act": extract_act(name, loc, how),
                "ign_url": IGN_CATEGORY_URLS["music-records"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()

    flush()
    save("music-records.json", {"id": "music-records", "name": "Music Records", "ign_url": IGN_CATEGORY_URLS["music-records"], "items": items})

# ── OUTFITS ───────────────────────────────────────────────────────────────────
def convert_outfits():
    df = pd.read_excel(SRC, sheet_name="Outfits", header=None)
    items = []
    current_character = None

    for i, row in df.iterrows():
        if i < 2: continue
        name = clean(row[0])
        loc  = clean(row[2])
        how  = clean(row[4])
        comp = str(row[10]).strip().lower() == "true" if not pd.isna(row[10]) else False

        if name and not loc and not how and name not in ("Outfit", "Location", "How to Find"):
            current_character = name
            continue

        if name and name not in ("Outfit", "Location", "How to Find") and current_character:
            display_name = clean_name(name)
            items.append({
                "id": slug("o", "o", len(items)),
                "name": display_name,
                "character": current_character,
                "location": loc,
                "how_to_find": how,
                "missable": is_missable(name, loc),
                "act": extract_act(name, loc, how),
                "ign_url": IGN_CATEGORY_URLS["outfits"],
                "completed": comp,
            })

    save("outfits.json", {"id": "outfits", "name": "Outfits", "ign_url": IGN_CATEGORY_URLS["outfits"], "items": items})

# ── PAINT CAGES ───────────────────────────────────────────────────────────────
def convert_paint_cages():
    df = pd.read_excel(SRC, sheet_name="Paint Cages", header=None)
    items = []
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        loc     = clean(row[0])
        how     = clean(row[2])
        rewards = clean(row[6])
        comp    = str(row[8]).strip().lower() == "true" if not pd.isna(row[8]) else False

        if loc and loc not in ("Location", "How to Find"):
            flush()
            current = {
                "id": slug("pc", "pc", len(items)),
                "location": loc,
                "how_to_find": how,
                "rewards": rewards,
                "missable": False,
                "ign_url": IGN_CATEGORY_URLS["paint-cages"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()

    flush()
    save("paint-cages.json", {"id": "paint-cages", "name": "Paint Cages", "ign_url": IGN_CATEGORY_URLS["paint-cages"], "items": items})

# ── PETANKS ───────────────────────────────────────────────────────────────────
def convert_petanks():
    df = pd.read_excel(SRC, sheet_name="Petanks", header=None)
    items = []
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        loc     = clean(row[0])
        how     = clean(row[2])
        rewards = clean(row[11])
        comp    = str(row[14]).strip().lower() == "true" if not pd.isna(row[14]) else False

        if loc and loc not in ("Location", "How to Find"):
            flush()
            current = {
                "id": slug("pt", "pt", len(items)),
                "location": loc,
                "how_to_find": how,
                "rewards": rewards,
                "missable": False,
                "ign_url": IGN_CATEGORY_URLS["petanks"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()
        elif current and rewards:
            current["rewards"] = (current["rewards"] + " " + rewards).strip()

    flush()
    save("petanks.json", {"id": "petanks", "name": "Petanks", "ign_url": IGN_CATEGORY_URLS["petanks"], "items": items})

# ── PICTOS ────────────────────────────────────────────────────────────────────
MISSABLE_PICTOS = {"Exposing Attack", "Auto Powerful"}

def convert_pictos():
    df = pd.read_excel(SRC, sheet_name="Pictos", header=None)
    items = []
    for i, row in df.iterrows():
        if i < 2: continue
        name       = clean(row[0])
        effect     = clean(row[1])
        lumina_cost= clean(row[2])
        location   = clean(row[3])
        how        = clean(row[4])
        collected_raw = row[5]
        lumina_raw    = row[6]

        collected = False if pd.isna(collected_raw) else (str(collected_raw).strip() not in ("0", "False", "false", ""))
        lumina    = str(lumina_raw).strip().lower() == "true" if not pd.isna(lumina_raw) else False

        if name and name not in ("Picto", "Effect", "Lumina cost"):
            display_name = clean_name(name)
            if lumina:
                state = "lumina"
            elif collected:
                state = "collected"
            else:
                state = "none"

            items.append({
                "id": slug("p", "p", len(items)),
                "name": display_name,
                "effect": effect,
                "lumina_cost": lumina_cost,
                "location": location,
                "how_to_find": how,
                "missable": display_name in MISSABLE_PICTOS or is_missable(name, location),
                "act": extract_act(name, location, how),
                "ign_url": IGN_CATEGORY_URLS["pictos"],
                "state": state,
            })

    save("pictos.json", {"id": "pictos", "name": "Pictos", "ign_url": IGN_CATEGORY_URLS["pictos"], "items": items})

# ── QUESTS ────────────────────────────────────────────────────────────────────
def convert_quests():
    df = pd.read_excel(SRC, sheet_name="Quests", header=None)
    items = []
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        name    = clean(row[0])
        loc     = clean(row[2])
        how     = clean(row[4])
        rewards = clean(row[13])
        comp    = str(row[16]).strip().lower() == "true" if not pd.isna(row[16]) else False

        if name and name not in ("Quest", "Location", "How to Complete"):
            flush()
            ign = QUEST_IGN.get(name) or IGN_CATEGORY_URLS["quests"]
            current = {
                "id": slug("q", "q", len(items)),
                "name": name,
                "location": loc,
                "how_to_complete": how,
                "rewards": rewards,
                "missable": is_missable(name, loc),
                "act": extract_act(name, loc, how),
                "ign_url": ign,
                "completed": comp,
            }
        elif current and how:
            current["how_to_complete"] = (current["how_to_complete"] + " " + how).strip()
        elif current and rewards:
            current["rewards"] = (current["rewards"] + " " + rewards).strip()

    flush()
    save("quests.json", {"id": "quests", "name": "Quests", "ign_url": IGN_CATEGORY_URLS["quests"], "items": items})

# ── TINT UPGRADES ─────────────────────────────────────────────────────────────
def convert_tint_upgrades():
    # Each row with a location is a separate collectable, even if the item name
    # is shared. Rows without a location are continuation of how_to_find text.
    df = pd.read_excel(SRC, sheet_name="Tint Upgrades", header=None)
    items = []
    current_name = None
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 2: continue
        name = clean(row[0])
        loc  = clean(row[2])
        how  = clean(row[4])
        comp = str(row[13]).strip().lower() == "true" if not pd.isna(row[13]) else False

        if name and name not in ("Item", "Location", "How to Find"):
            current_name = name

        # A new location on any row (with or without a name) = new item
        if loc and loc not in ("Location",) and current_name:
            flush()
            current = {
                "id": slug("tu", "tu", len(items)),
                "name": current_name,
                "location": loc,
                "how_to_find": how,
                "missable": False,
                "ign_url": IGN_CATEGORY_URLS["tint-upgrades"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()

    flush()
    save("tint-upgrades.json", {"id": "tint-upgrades", "name": "Tint Upgrades", "ign_url": IGN_CATEGORY_URLS["tint-upgrades"], "items": items})

# ── WEAPONS ───────────────────────────────────────────────────────────────────
WEAPON_SKIP = {"Weapon", "Location", "How to Find", "Collected?", "Damage Type",
               "Max Damage", "Scaling (S/A)", "Passives", "You have found"}

def convert_weapons():
    df = pd.read_excel(SRC, sheet_name="Weapons", header=None)
    items = []
    current_character = None
    current = None

    def flush():
        if current:
            items.append(current.copy())

    for i, row in df.iterrows():
        if i < 1: continue  # skip only the totals row (row 0)
        name        = clean(row[0])
        loc         = clean(row[2])
        how         = clean(row[4])
        comp        = str(row[10]).strip().lower() == "true" if not pd.isna(row[10]) else False
        dmg_type    = clean(row[12])
        max_dmg     = clean(row[14])
        scaling     = clean(row[16])
        passives    = clean(row[17]) + " " + clean(row[18])
        passives    = passives.strip()

        # Skip the column-header row
        if name in WEAPON_SKIP: continue

        # Character header row: has a name, no location, no how_to_find, no damage_type
        if name and not loc and not how and not dmg_type:
            flush(); current = None
            current_character = name
            continue

        if name and name not in ("Weapon", "Location", "How to Find", "Damage Type", "Max Damage", "Scaling (S/A)", "Passives"):
            flush()
            current = {
                "id": slug("w", "w", len(items)),
                "name": name,
                "character": current_character or "",
                "location": loc,
                "how_to_find": how,
                "damage_type": dmg_type,
                "max_damage": max_dmg,
                "scaling": scaling,
                "passives": passives,
                "missable": is_missable(name, loc),
                "act": extract_act(name, loc, how),
                "ign_url": IGN_CATEGORY_URLS["weapons"],
                "completed": comp,
            }
        elif current and how:
            current["how_to_find"] = (current["how_to_find"] + " " + how).strip()
        elif current and passives.strip():
            current["passives"] = (current["passives"] + " " + passives).strip()
        elif current and loc and not current["location"]:
            current["location"] = loc

    flush()
    save("weapons.json", {"id": "weapons", "name": "Weapons", "ign_url": IGN_CATEGORY_URLS["weapons"], "items": items})

# ── CATEGORIES INDEX ──────────────────────────────────────────────────────────
def build_categories():
    categories = [
        {"id": "bosses-main",     "name": "Main Bosses",         "icon": "shield",   "file": "bosses-main.json",     "ign_url": IGN_CATEGORY_URLS["bosses-main"]},
        {"id": "bosses-optional", "name": "Optional Bosses",     "icon": "sword",    "file": "bosses-optional.json", "ign_url": IGN_CATEGORY_URLS["bosses-optional"]},
        {"id": "endless-tower",   "name": "Endless Tower",       "icon": "layers",   "file": "endless-tower.json",   "ign_url": IGN_CATEGORY_URLS["endless-tower"]},
        {"id": "journals",        "name": "Expedition Journals", "icon": "book",     "file": "journals.json",        "ign_url": IGN_CATEGORY_URLS["journals"]},
        {"id": "haircuts",        "name": "Haircuts",            "icon": "scissors", "file": "haircuts.json",        "ign_url": IGN_CATEGORY_URLS["haircuts"]},
        {"id": "lost-gestrals",   "name": "Lost Gestrals",       "icon": "search",   "file": "lost-gestrals.json",   "ign_url": IGN_CATEGORY_URLS["lost-gestrals"]},
        {"id": "mimes",           "name": "Mimes",               "icon": "mask",     "file": "mimes.json",           "ign_url": IGN_CATEGORY_URLS["mimes"]},
        {"id": "monoco-skills",   "name": "Monoco Skills",       "icon": "zap",      "file": "monoco-skills.json",   "ign_url": IGN_CATEGORY_URLS["monoco-skills"]},
        {"id": "music-records",   "name": "Music Records",       "icon": "music",    "file": "music-records.json",   "ign_url": IGN_CATEGORY_URLS["music-records"]},
        {"id": "outfits",         "name": "Outfits",             "icon": "shirt",    "file": "outfits.json",         "ign_url": IGN_CATEGORY_URLS["outfits"]},
        {"id": "paint-cages",     "name": "Paint Cages",         "icon": "lock",     "file": "paint-cages.json",     "ign_url": IGN_CATEGORY_URLS["paint-cages"]},
        {"id": "petanks",         "name": "Petanks",             "icon": "target",   "file": "petanks.json",         "ign_url": IGN_CATEGORY_URLS["petanks"]},
        {"id": "pictos",          "name": "Pictos",              "icon": "image",    "file": "pictos.json",          "ign_url": IGN_CATEGORY_URLS["pictos"]},
        {"id": "quests",          "name": "Quests",              "icon": "map",      "file": "quests.json",          "ign_url": IGN_CATEGORY_URLS["quests"]},
        {"id": "tint-upgrades",   "name": "Tint Upgrades",       "icon": "droplet",  "file": "tint-upgrades.json",   "ign_url": IGN_CATEGORY_URLS["tint-upgrades"]},
        {"id": "weapons",         "name": "Weapons",             "icon": "crosshair","file": "weapons.json",         "ign_url": IGN_CATEGORY_URLS["weapons"]},
    ]
    path = os.path.join(OUT, "categories.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)
    print(f"  ✓ categories.json ({len(categories)} categories)")

# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Converting Excel → JSON...")
    convert_bosses()
    convert_endless_tower()
    convert_journals()
    convert_haircuts()
    convert_lost_gestrals()
    convert_mimes()
    convert_monoco_skills()
    convert_music_records()
    convert_outfits()
    convert_paint_cages()
    convert_petanks()
    convert_pictos()
    convert_quests()
    convert_tint_upgrades()
    convert_weapons()
    build_categories()
    print("\nDone.")
