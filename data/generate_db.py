import json, random

sub_areas = [
    {"id": "startorch", "name": "Startorch Academy", "desc": "Akademi riset frekuensi bawah tanah pusat Lahai-Roi", "bounds": [180, 260, 480, 560]},
    {"id": "rebirth", "name": "Rebirth Uplands", "desc": "Teras geologis bertingkat dengan flora fosil kristal", "bounds": [500, 200, 780, 480]},
    {"id": "etching", "name": "Etching Plains", "desc": "Dataran luas terukir gelombang suara purba", "bounds": [220, 600, 520, 920]},
    {"id": "mawburrow", "name": "Mawburrow Desert", "desc": "Gurun pasir resonator bawah tanah sarang Thundstaff", "bounds": [540, 620, 840, 950]},
    {"id": "stagnant", "name": "Stagnant Run", "desc": "Lembah aliran tacetite beku dengan gas korosi", "bounds": [80, 300, 200, 650]},
    {"id": "bjartr", "name": "Bjartr Woods", "desc": "Hutan lumut bioluminescent bersuhu hangat di bawah es", "bounds": [780, 260, 980, 580]},
    {"id": "fangspire", "name": "Fangspire Chasm", "desc": "Jurang vertikal taring stalaktit kristal", "bounds": [340, 80, 620, 220]},
    {"id": "starward", "name": "Starward Riseway", "desc": "Jalur pendakian reruntuhan elevator peradaban lama", "bounds": [800, 600, 980, 880]},
    {"id": "giants_gaze", "name": "Giant's Gaze", "desc": "Observatorium kubah raksasa pemantau inti Roya Frostlands", "bounds": [460, 440, 620, 600]}
]

# Acquisition templates
ACQUISITIONS = {
    "open_world": {
        "badge": "🗺️ Terbuka di Map",
        "color": "#00E5FF",
        "icon": "map-pin",
        "types": [
            ("Free Standing", "Terletak bebas di puncak pilar kristal/atap reruntuhan."),
            ("Tacet Monster Guarded", "Dijaga gerombolan Tacet Discord (Havoc Warrior & Dreadmane). Kalahkan semua musuh untuk membuka segel."),
            ("Bramble Thorns", "Terkunci tanaman berduri merah. Gunakan Explosive Charge / Tacetite Grenade untuk membakar duri.")
        ]
    },
    "quest": {
        "badge": "📜 Terkunci Misi / Quest",
        "color": "#FFD166",
        "icon": "scroll",
        "types": [
            ("Main Story Act VII", "Hadiah langsung setelah menyelesaikan cutscene Rekonstruksi Inti Startorch."),
            ("Exploration Quest: Echoes of the Deep", "Muncul di altar setelah Yang mengalirkan 3 Frekuensi Resonan di Fangspire."),
            ("Side Quest: Roya's Lost Caravan", "Diberikan oleh NPC Peneliti Linna setelah menemukan 4 kargo perbekalan yang hilang di Mawburrow."),
            ("Companion Quest: Echo of Frost", "Buka brankas laboratorium rahasia selama investigasi misi cerita.")
        ]
    },
    "hidden_challenge": {
        "badge": "🧩 Hidden Puzzle & Minigame",
        "color": "#FF4D6D",
        "icon": "puzzle-piece",
        "types": [
            ("Smartprint Cube Reboot", "Putar kubus holographic 3x3 agar seluruh matriks pola glyph bercahaya sinkron."),
            ("Mutterfly Guiding", "Ikuti 3 kupu-kupu sonik bioluminescent ke sarang kristal untuk membuka peti."),
            ("Blobfly Precision Snipe", "Tembak Blobfly kamuflase di dinding tebing tinggi menggunakan karakter Pistol (Chixia/Mortefi)."),
            ("Pressure Plate Sequencing", "Injak 4 pelat resonan secara berurutan sesuai pola nada lonceng akustik."),
            ("Tacetite Cleanse Trial", "Bersihkan 3 titik tumor polusi sebelum batas waktu 60 detik habis.")
        ]
    }
}

TIERS = {
    "basic": {"name": "Basic Supply Chest", "color": "#8E9AAF", "astrite": 5, "shell": 2000, "exp": 10},
    "standard": {"name": "Standard Supply Chest", "color": "#06D6A0", "astrite": 10, "shell": 5000, "exp": 20},
    "advanced": {"name": "Advanced Supply Chest", "color": "#118AB2", "astrite": 20, "shell": 10000, "exp": 30},
    "premium": {"name": "Premium Supply Chest", "color": "#9D4EDD", "astrite": 40, "shell": 20000, "exp": 50},
    "tidal_heritage": {"name": "Golden Tidal Heritage", "color": "#FFB703", "astrite": 50, "shell": 30000, "exp": 60},
    "sonance_casket": {"name": "Sonance Casket", "color": "#00F5D4", "astrite": 0, "shell": 0, "exp": 100}
}

items = []
id_counter = 1

random.seed(1337)

for area in sub_areas:
    min_x, min_y, max_x, max_y = area["bounds"]
    # Generate balanced mix for each sub-area
    counts = {
        "open_world": random.randint(8, 14),
        "quest": random.randint(4, 7),
        "hidden_challenge": random.randint(6, 10)
    }

    for acq_type, count in counts.items():
        acq_info = ACQUISITIONS[acq_type]
        for i in range(count):
            # Select Tier
            tier_weights = [("basic", 0.40), ("standard", 0.30), ("advanced", 0.18), ("premium", 0.08), ("tidal_heritage", 0.04)]
            r = random.random()
            acc = 0
            tier_id = "basic"
            for t_k, w in tier_weights:
                acc += w
                if r <= acc:
                    tier_id = t_k
                    break
            
            # Special logic: Quests & Hidden Challenges have higher chance for Advanced/Premium
            if acq_type == "quest" and tier_id in ["basic"]:
                tier_id = random.choice(["standard", "advanced", "premium"])
            elif acq_type == "hidden_challenge" and tier_id in ["basic"]:
                tier_id = random.choice(["standard", "advanced", "tidal_heritage"])

            tier_meta = TIERS[tier_id]
            sub_type, guide_desc = random.choice(acq_info["types"])

            x = round(random.uniform(min_x, max_x), 1)
            y = round(random.uniform(min_y, max_y), 1)

            item = {
                "id": f"wuwa_{id_counter:04d}",
                "name": f"{tier_meta['name']} #{id_counter}",
                "area_id": area["id"],
                "area_name": area["name"],
                "tier": tier_id,
                "tier_name": tier_meta["name"],
                "acquisition": acq_type,
                "acquisition_badge": acq_info["badge"],
                "sub_type": sub_type,
                "x": x,
                "y": y,
                "altitude": f"{random.choice(['Elevasi Tinggi (Tebing/Atap)', 'Permukaan Tanah', 'Gua Bawah Tanah / Sub-level', 'Teras Jurang'])}",
                "guide": guide_desc,
                "rewards": {
                    "astrite": tier_meta["astrite"],
                    "shell_credit": tier_meta["shell"],
                    "union_exp": tier_meta["exp"],
                    "wood_casket": 1 if tier_id in ["advanced", "premium", "tidal_heritage"] else 0
                }
            }
            items.append(item)
            id_counter += 1

    # Add 2 Sonance Caskets per area
    for s_i in range(2):
        x = round(random.uniform(min_x, max_x), 1)
        y = round(random.uniform(min_y, max_y), 1)
        items.append({
            "id": f"wuwa_{id_counter:04d}",
            "name": f"Sonance Casket: {area['name']} #{s_i + 1}",
            "area_id": area["id"],
            "area_name": area["name"],
            "tier": "sonance_casket",
            "tier_name": "Sonance Casket",
            "acquisition": "open_world",
            "acquisition_badge": "🔮 Relic Koleksi",
            "sub_type": "High Elevation Floating Casket",
            "x": x,
            "y": y,
            "altitude": "Mengapung di udara / Puncak pilar",
            "guide": "Gunakan Grapple Hook / Flight Glider dari tebing tertinggi di sekitar untuk menyambar peti melayang ini.",
            "rewards": {
                "astrite": 0,
                "shell_credit": 10000,
                "union_exp": 100,
                "wood_casket": 0
            }
        })
        id_counter += 1

db = {
    "version": "WuWa 3.8 Lahai-Roi & Frostlands Edition",
    "total_markers": len(items),
    "sub_areas": sub_areas,
    "markers": items
}

with open('/home/hatch/workspace/wuwa-interactive-map/data/chests.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Generated {len(items)} high-fidelity markers for Lahai-Roi map!")
