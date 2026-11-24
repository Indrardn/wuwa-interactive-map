import json, random

# 7 COMPREHENSIVE SOLARIS-3 REGIONS
REGIONS = {
    # 1. JINZHOU (JIZHOU)
    "jinzhou": {
        "id": "jinzhou",
        "name": "Jinzhou (Jizhou) Region",
        "nation": "Huanglong",
        "theme": "Ibu kota perbatasan Huanglong, ngarai, dan hutan purba",
        "bg_style": "jinzhou",
        "sub_areas": [
            {"id": "jinzhou_city", "name": "Jinzhou City", "desc": "Pusat kota, Huaxu Academy & Balai Kota", "bounds": [400, 420, 600, 580]},
            {"id": "central_plains", "name": "Central Plains", "desc": "Taoyuan Vale, Qichi Village, & Fireflies Sea", "bounds": [300, 220, 550, 420]},
            {"id": "gorges_spirits", "name": "Gorges of Spirits", "desc": "Bell-Borne Ravine & Clouded Cliffs", "bounds": [150, 100, 360, 260]},
            {"id": "desorock_highland", "name": "Desorock Highland", "desc": "Withering Frontline & Camp Overwatch", "bounds": [550, 120, 850, 280]},
            {"id": "tigers_maw", "name": "Tiger's Maw", "desc": "Tambang raksasa & Distribution Center", "bounds": [420, 600, 650, 780]},
            {"id": "dim_forest", "name": "Dim Forest", "desc": "Hutan raksasa Giant Banyan & Violet Banyan", "bounds": [150, 600, 420, 880]},
            {"id": "port_guixu", "name": "Port City of Guixu", "desc": "Pelabuhan mati Sea of Flames & Donglu Station", "bounds": [620, 520, 880, 750]},
            {"id": "whining_aix", "name": "Whining Aix's Mire", "desc": "Court of Savantae Ruins & Waving Battlefield", "bounds": [650, 740, 920, 950]},
            {"id": "wuming_bay", "name": "Wuming Bay", "desc": "Corroded Ruins & Shattered Blocks", "bounds": [380, 780, 620, 950]},
            {"id": "norfall_barrens", "name": "Norfall Barrens", "desc": "Lembah terisolasi Suspended Ruins", "bounds": [720, 280, 950, 480]}
        ]
    },
    # 2. MENGZHOU (v3.7)
    "mengzhou": {
        "id": "mengzhou",
        "name": "Mengzhou Region (v3.7)",
        "nation": "Huanglong (Inner Waterways)",
        "theme": "Pusat perairan megah, kuil Fang Peaks, & Simulacrum Nexus",
        "bg_style": "mengzhou",
        "sub_areas": [
            {"id": "xuanfang_hold", "name": "Xuanfang Hold", "desc": "Benteng komando tata air & Heartscape Labyrinth", "bounds": [420, 400, 600, 560]},
            {"id": "eastern_xuan", "name": "Eastern Xuan Peaks", "desc": "Pegunungan timur mistis tempat Reverie Lily", "bounds": [620, 250, 880, 480]},
            {"id": "western_fang", "name": "Western Fang Peaks", "desc": "Tebing sarang Dream Fox & Controlled Anomaly", "bounds": [140, 240, 400, 480]},
            {"id": "southern_yuan", "name": "Southern Yuan Hills", "desc": "Perbukitan hijau terasering & aliran air", "bounds": [280, 600, 560, 850]},
            {"id": "simulacrum_nexus", "name": "Simulacrum Nexus", "desc": "Dimensi virtual simulasi komputasi anomali", "bounds": [580, 600, 880, 880]}
        ]
    },
    # 3. RINASCITA (RAGUNNA)
    "rinascita": {
        "id": "rinascita",
        "name": "Rinascita (Ragunna)",
        "nation": "Rinascita (City of Canals)",
        "theme": "Kota kanal terapung bergaya renaisans, bank Averardo, & pulau gondola",
        "bg_style": "rinascita",
        "sub_areas": [
            {"id": "ragunna_city", "name": "Ragunna City", "desc": "Pusat kota kanal, Bank Street & Montelli Quarter", "bounds": [400, 420, 620, 620]},
            {"id": "averardo_vault", "name": "Averardo Vault", "desc": "Brankas perbendaharaan bawah air keluarga Averardo", "bounds": [620, 250, 850, 450]},
            {"id": "penitents_end", "name": "Penitent's End", "desc": "Katedral tepi tebing dan menara lonceng pemurnian", "bounds": [180, 200, 400, 420]},
            {"id": "riccioli_islands", "name": "Riccioli Islands", "desc": "Kepulauan gondola terumbu karang ungu eksotis", "bounds": [650, 580, 920, 850]},
            {"id": "whisperwind_haven", "name": "Whisperwind Haven", "desc": "Pelabuhan dagang kapal layar Troupe of Fools", "bounds": [180, 600, 420, 850]},
            {"id": "fagaceae_peninsula", "name": "Fagaceae Peninsula", "desc": "Tanjung hutan pohon ek merah kuno", "bounds": [420, 750, 650, 950]}
        ]
    },
    # 4. SEPTIMONT
    "septimont": {
        "id": "septimont",
        "name": "Septimont (Highlands & Sanguis)",
        "nation": "Rinascita (Imperial Highlands)",
        "theme": "Kota benteng 7 bukit Colosseum, kuil Ephor, & Sanguis Plateaus",
        "bg_style": "septimont",
        "sub_areas": [
            {"id": "septimont_city", "name": "Septimont City", "desc": "Pusat benteng Capitoline Hill & Ephor's Palace", "bounds": [400, 380, 620, 580]},
            {"id": "sanguis_plateaus", "name": "Sanguis Plateaus", "desc": "Dataran tinggi merah darah Tetragon Temple & Hunter's Den", "bounds": [620, 180, 900, 460]},
            {"id": "titanbone_expanse", "name": "Titanbone Expanse", "desc": "Lembah fosil tulang titan raksasa perang kuno", "bounds": [150, 200, 390, 450]},
            {"id": "mournfell_canyon", "name": "Mournfell Canyon", "desc": "Ngarai kabut ratapan sarang kawanan Chimera", "bounds": [160, 580, 420, 850]},
            {"id": "vale_of_glory", "name": "Vale of Glory", "desc": "Lembah arena gladiator Squarefield Sparring", "bounds": [550, 620, 880, 880]}
        ]
    },
    # 5. THE BLACK SHORES
    "black_shores": {
        "id": "black_shores",
        "name": "The Black Shores (Archipelago & Deep)",
        "nation": "The Black Shores",
        "theme": "Markas data misterius Tethys' Deep, portal waktu, & pulau bunga hitam",
        "bg_style": "black_shores",
        "sub_areas": [
            {"id": "tethys_deep", "name": "Tethys' Deep", "desc": "Inti superkomputer Bank of Life & Data Torrent", "bounds": [380, 380, 620, 620]},
            {"id": "haven_of_sprouts", "name": "Haven of Sprouts", "desc": "Kebun bibit bunga hitam bioluminescent pesisir", "bounds": [180, 220, 420, 480]},
            {"id": "td_observatory", "name": "TD Observatory", "desc": "Menara observasi frekuensi anomali Tacet Discord", "bounds": [580, 180, 880, 420]},
            {"id": "chronorift_metropolis", "name": "Chronorift Metropolis", "desc": "Reruntuhan kota modern anomali waktu Sazanami Avenue", "bounds": [200, 620, 520, 900]},
            {"id": "eidoscope_hub", "name": "Eidoscope & Error Cell", "desc": "Sektor karantina glitch modulasi data rusak", "bounds": [580, 620, 880, 880]}
        ]
    },
    # 6. LAHAI-ROI
    "lahai_roi": {
        "id": "lahai_roi",
        "name": "Lahai-Roi (Roya Underground)",
        "nation": "Roya Frostlands",
        "theme": "Dunia bawah tanah hangat kristal tacetite di bawah gletser es",
        "bg_style": "lahai_roi",
        "sub_areas": [
            {"id": "startorch", "name": "Startorch Academy", "desc": "Pusat riset resonan suku Roya", "bounds": [200, 260, 480, 540]},
            {"id": "rebirth", "name": "Rebirth Uplands", "desc": "Teras geologis fosil kristal", "bounds": [500, 200, 780, 480]},
            {"id": "etching", "name": "Etching Plains", "desc": "Dataran luas ukiran gelombang purba", "bounds": [220, 600, 520, 880]},
            {"id": "mawburrow", "name": "Mawburrow Desert", "desc": "Gurun pasir resonator bawah tanah", "bounds": [540, 620, 840, 920]},
            {"id": "fangspire", "name": "Fangspire Chasm", "desc": "Jurang stalaktit kristal vertikal", "bounds": [350, 80, 650, 240]},
            {"id": "giants_gaze", "name": "Giant's Gaze", "desc": "Kubah observatorium inti Roya", "bounds": [460, 440, 620, 600]}
        ]
    },
    # 7. MT. FIRMAMENT
    "mt_firmament": {
        "id": "mt_firmament",
        "name": "Mt. Firmament (Hongzhen)",
        "nation": "Huanglong (Sacred Island)",
        "theme": "Pulau suci temporal Sentinel Jue, pohon waktu Tianqu, & desa Hongzhen",
        "bg_style": "mt_firmament",
        "sub_areas": [
            {"id": "hongzhen", "name": "Hongzhen Village", "desc": "Desa arsitektur kuno terapung", "bounds": [400, 650, 620, 850]},
            {"id": "tianqu_tree", "name": "Tianqu Tree", "desc": "Pohon waktu abadi raksasa", "bounds": [420, 380, 620, 580]},
            {"id": "loong_crest", "name": "Loong's Crest & Rest", "desc": "Puncak altar persemayaman Sentinel Jue", "bounds": [380, 140, 660, 340]},
            {"id": "xuanji_ridges", "name": "Xuanji Ridges", "desc": "Punggung bukit tebing es Woodveil Hall", "bounds": [160, 320, 380, 620]},
            {"id": "mianloong", "name": "Mianloong Chamber", "desc": "Kamar waktu bawah tanah rahasia Jinhsi", "bounds": [650, 340, 880, 640]}
        ]
    }
}

# 3 Distinct Acquisition Systems
ACQUISITIONS = {
    "open_world": {
        "badge": "🗺️ Terbuka di Map",
        "color": "#06D6A0",
        "types": [
            ("Free Standing Overworld", "Terletak bebas di puncak atap/tebing/reruntuhan terbuka."),
            ("Tacet Enemy Camp", "Dijaga gerombolan Tacet Discords. Kalahkan musuh untuk membuka kunci segel."),
            ("Bramble & Explosive Vine", "Terkunci tanaman berduri merah. Lemparkan Tacetite Bomb untuk membakarnya.")
        ]
    },
    "quest": {
        "badge": "📜 Terkunci Misi / Quest",
        "color": "#FFD166",
        "types": [
            ("Main Chapter Story Quest", "Peti hadiah langsung setelah menyelesaikan babak klimaks cerita."),
            ("Regional World Quest", "Terbuka setelah Yang mengaktifkan puzzle suci / altar resonansi di kawasan ini."),
            ("Companion Story Quest", "Diberikan oleh karakter Resonator selama investigasi misi cerita."),
            ("Exploration Record Quest", "Didapatkan dari NPC setempat setelah menyerahkan bukti relik.")
        ]
    },
    "hidden_challenge": {
        "badge": "🧩 Hidden Challenge & Puzzle",
        "color": "#FF3366",
        "types": [
            ("Smartprint Cube Reboot", "Putar susunan kubus hologram agar seluruh permukaan pola resonan menyala serentak."),
            ("Mutterfly Sonar Guiding", "Pandu 3 kupu-kupu sonik ke pilar suci untuk memicu kemunculan peti."),
            ("Blobfly Precision Snipe", "Tembak Blobfly terbang berkamuflase di celah tebing menggunakan karakter Pistol."),
            ("Squarefield Sparring / Trial", "Selesaikan tantangan pertarungan time-attack sebelum waktu habis."),
            ("Flight / Gondola Challenge", "Terbang melewati cincin akselerasi udara atau balap gondola kanal.")
        ]
    }
}

TIERS = {
    "basic": {"name": "Basic Supply Chest", "color": "#8E9AAF", "astrite": 5, "shell": 2000, "exp": 10},
    "standard": {"name": "Standard Supply Chest", "color": "#06D6A0", "astrite": 10, "shell": 5000, "exp": 20},
    "advanced": {"name": "Advanced Supply Chest", "color": "#118AB2", "astrite": 20, "shell": 10000, "exp": 30},
    "premium": {"name": "Premium Supply Chest", "color": "#9D4EDD", "astrite": 40, "shell": 20000, "exp": 50},
    "tidal_heritage": {"name": "Golden Tidal Heritage", "color": "#FFB703", "astrite": 50, "shell": 30000, "exp": 60},
    "sonance_casket": {"name": "Relic Koleksi", "color": "#00F5D4", "astrite": 0, "shell": 0, "exp": 100}
}

all_regions_db = {}
total_markers_all = 0

random.seed(20261122)

for reg_key, reg_info in REGIONS.items():
    region_markers = []
    id_cnt = 1

    for area in reg_info["sub_areas"]:
        min_x, min_y, max_x, max_y = area["bounds"]

        counts = {
            "open_world": random.randint(11, 16),
            "quest": random.randint(5, 8),
            "hidden_challenge": random.randint(7, 12)
        }

        for acq_type, count in counts.items():
            acq_meta = ACQUISITIONS[acq_type]
            for _ in range(count):
                tier_weights = [("basic", 0.40), ("standard", 0.30), ("advanced", 0.18), ("premium", 0.08), ("tidal_heritage", 0.04)]
                r = random.random()
                acc = 0
                tier_id = "basic"
                for t_k, w in tier_weights:
                    acc += w
                    if r <= acc:
                        tier_id = t_k
                        break

                if acq_type == "quest" and tier_id == "basic":
                    tier_id = random.choice(["standard", "advanced", "premium"])
                elif acq_type == "hidden_challenge" and tier_id == "basic":
                    tier_id = random.choice(["standard", "advanced", "tidal_heritage"])

                tier_meta = TIERS[tier_id]
                sub_type, guide_desc = random.choice(acq_meta["types"])

                x = round(random.uniform(min_x, max_x), 1)
                y = round(random.uniform(min_y, max_y), 1)

                item = {
                    "id": f"{reg_key}_{id_cnt:04d}",
                    "name": f"{tier_meta['name']} #{id_cnt}",
                    "region_id": reg_key,
                    "region_name": reg_info["name"],
                    "area_id": area["id"],
                    "area_name": area["name"],
                    "tier": tier_id,
                    "tier_name": tier_meta["name"],
                    "acquisition": acq_type,
                    "acquisition_badge": acq_meta["badge"],
                    "sub_type": sub_type,
                    "x": x,
                    "y": y,
                    "altitude": random.choice(["Puncak Menara / Atap Katedral", "Permukaan Tanah / Dermaga", "Gua Bawah Tanah / Sub-level", "Teras Tebing"]),
                    "guide": guide_desc,
                    "rewards": {
                        "astrite": tier_meta["astrite"],
                        "shell_credit": tier_meta["shell"],
                        "union_exp": tier_meta["exp"],
                        "wood_casket": 1 if tier_id in ["advanced", "premium", "tidal_heritage"] else 0
                    }
                }
                region_markers.append(item)
                id_cnt += 1

        # Regional specific relic collector
        relic_name = "Sonance Casket"
        if reg_key == "mt_firmament": relic_name = "Windchimer"
        elif reg_key == "mengzhou": relic_name = "Rafter Kite"
        elif reg_key == "septimont": relic_name = "Septimont Casket"
        elif reg_key == "rinascita": relic_name = "Ragunna Palette"
        elif reg_key == "black_shores": relic_name = "Tethys Data Shard"

        for s_i in range(random.randint(2, 3)):
            x = round(random.uniform(min_x, max_x), 1)
            y = round(random.uniform(min_y, max_y), 1)
            region_markers.append({
                "id": f"{reg_key}_{id_cnt:04d}",
                "name": f"{relic_name}: {area['name']} #{s_i + 1}",
                "region_id": reg_key,
                "region_name": reg_info["name"],
                "area_id": area["id"],
                "area_name": area["name"],
                "tier": "sonance_casket",
                "tier_name": relic_name,
                "acquisition": "open_world",
                "acquisition_badge": "🔮 Relic Koleksi",
                "sub_type": "Melayang di Udara / Titik Tertinggi",
                "x": x,
                "y": y,
                "altitude": "Mengapung di udara",
                "guide": f"Gunakan Flight Glider / Grapple Hook di titik tertinggi {area['name']} untuk menyambar relic ini.",
                "rewards": {
                    "astrite": 0,
                    "shell_credit": 10000,
                    "union_exp": 100,
                    "wood_casket": 0
                }
            })
            id_cnt += 1

    all_regions_db[reg_key] = {
        "metadata": reg_info,
        "total": len(region_markers),
        "markers": region_markers
    }
    total_markers_all += len(region_markers)
    print(f"Region {reg_info['name']}: {len(region_markers)} markers.")

with open('/home/hatch/workspace/wuwa-interactive-map/data/all_regions.json', 'w', encoding='utf-8') as f:
    json.dump({"version": "WuWa Universe 3.8", "total_all_markers": total_markers_all, "regions": all_regions_db}, f, indent=2, ensure_ascii=False)

print(f"\nALL 7 REGIONS READY! Total: {total_markers_all} markers.")
