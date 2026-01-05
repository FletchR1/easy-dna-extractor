"""
SNP Database - Known SNPs and their effects
==========================================

This database contains SNP information compiled from scientific literature.
For educational and curiosity purposes only.

Categories:
- interesting: Interesting combinations
- extreme_rare: Very rare (<1%)
- rare: Rare (<5%)
- appearance: Physical appearance
- personality: Personality traits
- disease: Health and disease risk
- food: Nutrition and metabolism
- fitness: Physical performance
- cognitive: Cognitive traits
- lifestyle: Lifestyle factors
- longevity: Longevity and aging
- immunity: Immune system
"""

SNP_DATABASE = {
    # ================================================================
    # EXTREME RARE - Very rare variants (<1%)
    # ================================================================
    "rs1805007": {
        "gene": "MC1R",
        "category": "extreme_rare",
        "title": "Red Hair Gene (R151C)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "You are not a red hair carrier.",
            },
            "CT": {
                "effect": "carrier",
                "description": "You are a carrier of the red hair gene. Your children may have red hair.",
            },
            "TT": {
                "effect": "positive",
                "description": "You have the red hair gene! Found in only 1-2% of the world population.",
            },
        },
        "frequency": "~2% (Northern Europe)",
    },
    "rs1800401": {
        "gene": "OCA2",
        "category": "extreme_rare",
        "title": "Blue Eye Color",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "You have dark eye color genes."},
            "CT": {
                "effect": "carrier",
                "description": "You are a carrier of light eye color.",
            },
            "TT": {
                "effect": "positive",
                "description": "You have blue/green eye color genes.",
            },
        },
        "frequency": "~8% worldwide",
    },
    "rs7495174": {
        "gene": "OCA2",
        "category": "extreme_rare",
        "title": "Green Eye Color",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "This variant does not contribute to green eye color.",
            },
            "AG": {
                "effect": "carrier",
                "description": "You are a heterozygous carrier for green eye color.",
            },
            "AA": {
                "effect": "positive",
                "description": "You have a rare variant associated with green eye color! Found in only 2% of the world population.",
            },
        },
        "frequency": "~2% worldwide",
    },
    "rs17822931": {
        "gene": "ABCC11",
        "category": "extreme_rare",
        "title": "Dry Earwax & Body Odor",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "You have wet/sticky earwax type (common worldwide).",
            },
            "CT": {
                "effect": "carrier",
                "description": "You are a carrier of dry earwax.",
            },
            "TT": {
                "effect": "positive",
                "description": "You have the dry earwax gene! You also produce less body odor. Common in East Asia, rare in Europe.",
            },
        },
        "frequency": "~5% (Europe), ~90% (East Asia)",
    },
    "rs11803731": {
        "gene": "TCHH",
        "category": "extreme_rare",
        "title": "Straight vs Curly Hair",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Straight hair tendency."},
            "AG": {"effect": "wavy", "description": "Wavy hair tendency."},
            "AA": {
                "effect": "curly",
                "description": "Curly hair tendency! Rare in European-origin populations.",
            },
        },
        "frequency": "~6% (Europe)",
    },
    "rs4778241": {
        "gene": "OCA2",
        "category": "extreme_rare",
        "title": "Light Skin Pigmentation",
        "risk_allele": "A",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal melanin production."},
            "AC": {
                "effect": "light",
                "description": "Slightly light skin pigmentation.",
            },
            "AA": {
                "effect": "very_light",
                "description": "Very light skin pigmentation. May have sun sensitivity.",
            },
        },
        "frequency": "~3% worldwide",
    },
    "rs1393350": {
        "gene": "TYR",
        "category": "extreme_rare",
        "title": "Tyrosinase Variant",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal tyrosinase activity."},
            "AG": {
                "effect": "carrier",
                "description": "Carrier of reduced tyrosinase activity.",
            },
            "AA": {
                "effect": "reduced",
                "description": "Significantly reduced tyrosinase. Associated with light eye color.",
            },
        },
        "frequency": "~4%",
    },
    "rs12203592": {
        "gene": "IRF4",
        "category": "extreme_rare",
        "title": "Freckle Formation",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Low freckle tendency."},
            "CT": {"effect": "moderate", "description": "Moderate freckle tendency."},
            "TT": {
                "effect": "high",
                "description": "High freckle tendency! Sun sensitivity may also be increased.",
            },
        },
        "frequency": "~3%",
    },
    # ================================================================
    # RARE - Rare variants (<5%)
    # ================================================================
    "rs1805008": {
        "gene": "MC1R",
        "category": "rare",
        "title": "Light Skin & Freckles (R160W)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "You do not carry the MC1R variant.",
            },
            "CT": {
                "effect": "carrier",
                "description": "You are a carrier of light skin and freckle tendency.",
            },
            "TT": {
                "effect": "positive",
                "description": "You have a variant associated with light skin, freckles, and sun sensitivity.",
            },
        },
        "frequency": "~4% (Europe)",
    },
    "rs12913832": {
        "gene": "HERC2",
        "category": "rare",
        "title": "Eye Color Main Determinant",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "positive",
                "description": "Variant strongly associated with blue eye color. This SNP is the main determinant of eye color.",
            },
            "AG": {
                "effect": "carrier",
                "description": "High probability of mixed eye color (green, hazel).",
            },
            "GG": {
                "effect": "normal",
                "description": "Associated with dark eye color (brown).",
            },
        },
        "frequency": "~20% (AA genotype)",
    },
    "rs12821256": {
        "gene": "KITLG",
        "category": "rare",
        "title": "Blonde Hair Gene",
        "risk_allele": "C",
        "variants": {
            "TT": {
                "effect": "normal",
                "description": "You have dark hair color genes.",
            },
            "CT": {
                "effect": "carrier",
                "description": "You are a carrier of blonde hair.",
            },
            "CC": {
                "effect": "positive",
                "description": "You have a variant associated with blonde hair color!",
            },
        },
        "frequency": "~5% worldwide",
    },
    "rs1805005": {
        "gene": "MC1R",
        "category": "rare",
        "title": "MC1R V60L Variant",
        "risk_allele": "T",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal MC1R function."},
            "GT": {
                "effect": "carrier",
                "description": "MC1R V60L carrier. Slight light skin tendency.",
            },
            "TT": {
                "effect": "variant",
                "description": "MC1R V60L variant. Predisposition to light skin and red/blonde hair tones.",
            },
        },
        "frequency": "~5%",
    },
    "rs16891982": {
        "gene": "SLC45A2",
        "category": "rare",
        "title": "Skin Color (MATP)",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Dark skin pigmentation."},
            "CG": {
                "effect": "light",
                "description": "Light skin pigmentation carrier.",
            },
            "CC": {
                "effect": "very_light",
                "description": "Light skin pigmentation! Common in Europe.",
            },
        },
        "frequency": "~5% worldwide (CC)",
    },
    "rs1426654": {
        "gene": "SLC24A5",
        "category": "rare",
        "title": "Skin Color Ana Geni",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "dark", "description": "Dark skin pigmentation genotype."},
            "AG": {"effect": "medium", "description": "Medium tone skin pigmentation."},
            "AA": {
                "effect": "light",
                "description": "Light skin pigmentation! Found in 98% of European-origin populations.",
            },
        },
        "frequency": "Europe ~98%, Africa ~5%",
    },
    "rs2228479": {
        "gene": "MC1R",
        "category": "rare",
        "title": "MC1R V92M Variant",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal MC1R."},
            "AG": {"effect": "carrier", "description": "V92M carrier."},
            "AA": {
                "effect": "variant",
                "description": "MC1R V92M variant. More common in East Asia.",
            },
        },
        "frequency": "~4% (Europe), ~15% (Asia)",
    },
    # ================================================================
    # APPEARANCE - Physical appearance traits
    # ================================================================
    "rs3827760": {
        "gene": "EDAR",
        "category": "appearance",
        "title": "Hair Thickness & Tooth Shape",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Thin-moderate thickness hair."},
            "AG": {"effect": "thick", "description": "Thick hair strand tendency."},
            "AA": {
                "effect": "very_thick",
                "description": "Very thick hair strands! Shovel-shaped front teeth and more sweat glands. Common in East Asia.",
            },
        },
        "frequency": "East Asia ~90%, Europe ~1%",
    },
    "rs17646946": {
        "gene": "LRRC34",
        "category": "appearance",
        "title": "Dimple Formation",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Dimple probability low."},
            "AG": {"effect": "likely", "description": "Dimple probability moderate."},
            "AA": {
                "effect": "dimples",
                "description": "Variant associated with dimple formation!",
            },
        },
        "frequency": "~20%",
    },
    "rs10427255": {
        "gene": "PRSS53",
        "category": "appearance",
        "title": "Hair Wave",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "straight", "description": "Straight hair tendency."},
            "CT": {"effect": "wavy", "description": "Wavy hair tendency."},
            "CC": {"effect": "curly", "description": "Curly/wavy hair tendency."},
        },
        "frequency": "~15%",
    },
    "rs4648379": {
        "gene": "WNT10A",
        "category": "appearance",
        "title": "Tooth and Hair Development",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal tooth and hair development.",
            },
            "AG": {"effect": "variant", "description": "Hafif variant carrier."},
            "AA": {
                "effect": "affected",
                "description": "Differences in tooth shape and hair structure may be.",
            },
        },
        "frequency": "~8%",
    },
    "rs10166942": {
        "gene": "TRPM8",
        "category": "appearance",
        "title": "Migraine Predisposition",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Low migraine risk."},
            "CT": {"effect": "moderate", "description": "Moderate migraine risk."},
            "TT": {
                "effect": "increased",
                "description": "Increased migraine risk. Cold sensitivity may also be affected.",
            },
        },
        "frequency": "~20%",
    },
    "rs7349332": {
        "gene": "FGFR2",
        "category": "appearance",
        "title": "Hairline Shape",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "straight", "description": "Straight hairline tendency."},
            "CT": {"effect": "mixed", "description": "Variable hairline."},
            "TT": {
                "effect": "widows_peak",
                "description": "V-shaped hairline (widow's peak) tendency.",
            },
        },
        "frequency": "~30%",
    },
    "rs17833789": {
        "gene": "PAX3",
        "category": "appearance",
        "title": "Earlobe Structure",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "attached", "description": "Attached earlobe tendency."},
            "CT": {"effect": "mixed", "description": "Variable earlobe structure."},
            "CC": {
                "effect": "detached",
                "description": "Free (hanging) earlobe tendency.",
            },
        },
        "frequency": "~40%",
    },
    "rs2238289": {
        "gene": "HERC2",
        "category": "appearance",
        "title": "Hair Rengi Tonu",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "dark", "description": "Dark hair tone tendency."},
            "AG": {"effect": "medium", "description": "Medium tone hair."},
            "AA": {"effect": "light", "description": "Light hair tone tendency."},
        },
        "frequency": "~25%",
    },
    # ================================================================
    # PERSONALITY - Personality traits
    # ================================================================
    "rs4680": {
        "gene": "COMT",
        "category": "personality",
        "title": "Warrior vs Strategist (COMT)",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "warrior",
                "description": '"Warrior" genotype: Better performance under stress, fast dopamine breakdown. Instant decisions and action-oriented.',
            },
            "AG": {
                "effect": "balanced",
                "description": "Dengeli: Both stress tolerance and strategic thinking capacity you have.",
            },
            "AA": {
                "effect": "worrier",
                "description": '"Stratejist" genotype: Slow dopamine breakdown, better memory and attention. Strong in planning and analytical thinking.',
            },
        },
        "frequency": "Her genotype ~%25-35",
    },
    "rs6265": {
        "gene": "BDNF",
        "category": "personality",
        "title": "Learning and Neuroplasticity",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "Normal BDNF production. Good neuroplasticity and learning capacity.",
            },
            "CT": {
                "effect": "reduced",
                "description": "Reduced BDNF production. Memory and learning may be slightly affected under stress.",
            },
            "TT": {
                "effect": "low",
                "description": "Low BDNF production. Exercise and meditation can increase BDNF levels.",
            },
        },
        "frequency": "~20% (T alleli)",
    },
    "rs53576": {
        "gene": "OXTR",
        "category": "personality",
        "title": "Empathy and Social Bonding",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "high_empathy",
                "description": "High empathy capacity. Strong in reading social cues and forming emotional bonds.",
            },
            "AG": {
                "effect": "moderate",
                "description": "Moderate empathy. Balanced in social skills.",
            },
            "AA": {
                "effect": "lower",
                "description": "Lower oxytocin receptor density. Independent and analytical thinking tendency.",
            },
        },
        "frequency": "~%30 (GG)",
    },
    "rs1800955": {
        "gene": "DRD4",
        "category": "personality",
        "title": "Novelty Seeking",
        "risk_allele": "C",
        "variants": {
            "TT": {
                "effect": "normal",
                "description": "Standard dopamine receptor activity. Satisfaction with routine.",
            },
            "CT": {"effect": "moderate", "description": "Moderate novelty seeking."},
            "CC": {
                "effect": "high",
                "description": "High novelty seeking! Adventure, new experiences and risk-taking tendency.",
            },
        },
        "frequency": "~25% (CC)",
    },
    "rs25531": {
        "gene": "SLC6A4",
        "category": "personality",
        "title": "Duygusal Hassasiyet (Serotonin)",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "lower",
                "description": "Low serotonin transporter activity. More sensitive to environmental factors you may be.",
            },
            "AG": {
                "effect": "moderate",
                "description": "Moderate serotonin transport capacity.",
            },
            "GG": {
                "effect": "normal",
                "description": "Normal serotonin transporter activity. Emotional resilience.",
            },
        },
        "frequency": "~40% (AA)",
    },
    "rs1799732": {
        "gene": "DRD2",
        "category": "personality",
        "title": "Reward Sensitivity",
        "risk_allele": "G",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal reward response."},
            "CG": {
                "effect": "enhanced",
                "description": "Increased reward sensitivity.",
            },
            "GG": {
                "effect": "high",
                "description": "High reward sensitivity. You may enjoy positive experiences more.",
            },
        },
        "frequency": "~20%",
    },
    "rs1800497": {
        "gene": "DRD2/ANKK1",
        "category": "personality",
        "title": "Dopamine Receptor Density (Taq1A)",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal dopamine receptor density. Standard reward response.",
            },
            "AG": {
                "effect": "reduced",
                "description": "Reduced D2 receptor density. More reward seeking may be.",
            },
            "AA": {
                "effect": "low",
                "description": "Low D2 receptor density. Novelty and excitement seeking may be high.",
            },
        },
        "frequency": "~20% (A alleli)",
    },
    "rs7794745": {
        "gene": "CNTNAP2",
        "category": "personality",
        "title": "Language and Communication Ability",
        "risk_allele": "T",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal language processing."},
            "AT": {
                "effect": "variant",
                "description": "Different language processing style.",
            },
            "TT": {
                "effect": "enhanced",
                "description": "Differences in language learning and communication may be.",
            },
        },
        "frequency": "~25%",
    },
    "rs2760118": {
        "gene": "SIRT1",
        "category": "personality",
        "title": "Stress Resilience",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal stress response."},
            "CT": {
                "effect": "resilient",
                "description": "Increased stress resilience.",
            },
            "CC": {
                "effect": "high_resilience",
                "description": "High stress resilience! Better coping in difficult situations.",
            },
        },
        "frequency": "~15%",
    },
    "rs6313": {
        "gene": "HTR2A",
        "category": "personality",
        "title": "Serotonin Receptor (5-HT2A)",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal serotonin receptor activity.",
            },
            "AG": {
                "effect": "variant",
                "description": "Different serotonin receptor activity.",
            },
            "AA": {
                "effect": "altered",
                "description": "Altered serotonin receptor activity. Associated with mood and anxiety may be.",
            },
        },
        "frequency": "~35%",
    },
    "rs2030324": {
        "gene": "SLC6A4",
        "category": "personality",
        "title": "Serotonin Transporter Variant",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "Normal serotonin transporter function.",
            },
            "CT": {
                "effect": "variant",
                "description": "Different serotonin transporter activity.",
            },
            "TT": {
                "effect": "altered",
                "description": "Altered serotonin transporter activity.",
            },
        },
        "frequency": "~30%",
    },
    "rs1006737": {
        "gene": "CACNA1C",
        "category": "personality",
        "title": "Emotional Processing",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal emotional processing."},
            "AG": {
                "effect": "sensitive",
                "description": "More sensitive emotional processing.",
            },
            "AA": {
                "effect": "highly_sensitive",
                "description": "Intense emotional experiences. May be associated with artistic abilities.",
            },
        },
        "frequency": "~25%",
    },
    # ================================================================
    # DISEASE - Disease risk
    # ================================================================
    "rs1801133": {
        "gene": "MTHFR",
        "category": "disease",
        "title": "MTHFR C677T Variant",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal MTHFR enzyme activity. Folate metabolism normal.",
            },
            "AG": {
                "effect": "reduced",
                "description": "~35% reduced enzim activity. Folik asit takviyesi may be beneficial.",
            },
            "AA": {
                "effect": "significantly_reduced",
                "description": "~70% reduced enzim activity. Metilfolat formu recommended. Homosistein seviyeleri kontrol edilmeli.",
            },
        },
        "frequency": "~10% (AA), ~40% (AG)",
    },
    "rs1801131": {
        "gene": "MTHFR",
        "category": "disease",
        "title": "MTHFR A1298C Variant",
        "risk_allele": "G",
        "variants": {
            "TT": {
                "effect": "normal",
                "description": "Normal MTHFR enzyme activity (at this position).",
            },
            "GT": {"effect": "reduced", "description": "Hafif reduced enzim activity."},
            "GG": {
                "effect": "significantly_reduced",
                "description": "Reduced BH4 production. Neurotransmitter synthesis may be affected.",
            },
        },
        "frequency": "~10% (GG)",
    },
    "rs1799945": {
        "gene": "HFE",
        "category": "disease",
        "title": "Hemokromatoz (H63D)",
        "risk_allele": "G",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal iron metabolism."},
            "CG": {
                "effect": "carrier",
                "description": "Hemokromatoz carrier. Demir seviyeleri periyodik olarak kontrol edilmeli.",
            },
            "GG": {
                "effect": "risk",
                "description": "Hemochromatosis risk. Iron accumulation may be. Doctor monitoring recommended.",
            },
        },
        "frequency": "~5% (CG carrier)",
    },
    "rs1800562": {
        "gene": "HFE",
        "category": "disease",
        "title": "Hemokromatoz C282Y",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal HFE geni."},
            "AG": {
                "effect": "carrier",
                "description": "C282Y carrier. Usually does not cause problems alone.",
            },
            "AA": {
                "effect": "risk",
                "description": "Hereditary hemochromatosis risk high. Regular iron testing recommended.",
            },
        },
        "frequency": "~0.5% (AA)",
    },
    "rs7903146": {
        "gene": "TCF7L2",
        "category": "disease",
        "title": "Type 2 Diabetes Riski",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Ortalama Type 2 diabetes risk."},
            "CT": {
                "effect": "increased",
                "description": "~1.4x increased Type 2 diabetes risk. Healthy lifestyle important.",
            },
            "TT": {
                "effect": "high",
                "description": "~2x increased Type 2 diabetes risk. Regular blood sugar monitoring recommended.",
            },
        },
        "frequency": "~30% (T alleli)",
    },
    "rs429358": {
        "gene": "APOE",
        "category": "disease",
        "title": "APOE4 - Alzheimer Riski",
        "risk_allele": "C",
        "variants": {
            "TT": {
                "effect": "e3e3",
                "description": "APOE3/E3: Most common genotype. Average Alzheimer risk.",
            },
            "CT": {
                "effect": "e3e4",
                "description": "APOE3/E4: Increased Alzheimer risk. Attention to brain health recommended.",
            },
            "CC": {
                "effect": "e4e4",
                "description": "APOE4/E4: High Alzheimer risk. Omega-3, exercise and cognitive activity are protective.",
            },
        },
        "frequency": "~25% (E4 carrier)",
    },
    "rs7412": {
        "gene": "APOE",
        "category": "disease",
        "title": "APOE2 - Koruyucu Varyant",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "APOE3 or E4 genotype."},
            "CT": {
                "effect": "protective",
                "description": "APOE2 carrier. Protective effect against Alzheimer's!",
            },
            "TT": {
                "effect": "e2e2",
                "description": "APOE2/E2: Very rare. Low Alzheimer risk, but Type III hyperlipidemia risk.",
            },
        },
        "frequency": "~8% (APOE2 carrier)",
    },
    "rs10757278": {
        "gene": "CDKN2A/B",
        "category": "disease",
        "title": "Kalp Krizi Riski",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Low heart disease risk."},
            "AG": {
                "effect": "moderate",
                "description": "Moderate coronary artery disease risk.",
            },
            "GG": {
                "effect": "increased",
                "description": "~1.3x increased heart attack risk. Attention to cardiovascular health recommended.",
            },
        },
        "frequency": "~50% (G alleli)",
    },
    "rs1333049": {
        "gene": "9p21",
        "category": "disease",
        "title": "Coronary Artery Disease",
        "risk_allele": "C",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Low coronary artery disease risk.",
            },
            "CG": {"effect": "moderate", "description": "Moderate risk."},
            "CC": {
                "effect": "increased",
                "description": "Increased coronary artery disease risk. Cholesterol and blood pressure monitoring important.",
            },
        },
        "frequency": "~50%",
    },
    "rs2200733": {
        "gene": "4q25",
        "category": "disease",
        "title": "Atriyal Fibrilasyon Riski",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Low AF risk."},
            "CT": {
                "effect": "moderate",
                "description": "Moderate atrial fibrillation risk.",
            },
            "TT": {
                "effect": "increased",
                "description": "~1.7x increased atriyal fibrilasyon riski.",
            },
        },
        "frequency": "~15%",
    },
    "rs12255372": {
        "gene": "TCF7L2",
        "category": "disease",
        "title": "Type 2 Diabetes (2. variant)",
        "risk_allele": "T",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal diabetes risk."},
            "GT": {
                "effect": "increased",
                "description": "Increased Type 2 diabetes risk.",
            },
            "TT": {
                "effect": "high",
                "description": "High Type 2 diabetes risk. Blood sugar should be monitored regularly.",
            },
        },
        "frequency": "~25%",
    },
    "rs1800795": {
        "gene": "IL6",
        "category": "disease",
        "title": "Inflammation Tendency (IL-6)",
        "risk_allele": "G",
        "variants": {
            "CC": {
                "effect": "low_inflammation",
                "description": "Low IL-6 production. Low inflammation tendency.",
            },
            "CG": {"effect": "moderate", "description": "Moderate IL-6 production."},
            "GG": {
                "effect": "high_inflammation",
                "description": "High IL-6 production. Chronic inflammation risk. Anti-inflammatory diet beneficial.",
            },
        },
        "frequency": "~35%",
    },
    "rs1800629": {
        "gene": "TNF",
        "category": "disease",
        "title": "TNF-alpha Inflammation",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal TNF-alpha production."},
            "AG": {
                "effect": "elevated",
                "description": "Increased TNF-alpha production. Inflammation tendency.",
            },
            "AA": {
                "effect": "high",
                "description": "High TNF-alpha production. Autoimmune disease risk may be increased.",
            },
        },
        "frequency": "~15%",
    },
    "rs1042522": {
        "gene": "TP53",
        "category": "disease",
        "title": "Tumor Suppressor p53",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal p53 function (Arg/Arg)."},
            "CG": {"effect": "variant", "description": "Heterozigot (Arg/Pro)."},
            "CC": {
                "effect": "altered",
                "description": "Pro/Pro variant. Different apoptosis response.",
            },
        },
        "frequency": "~25%",
    },
    "rs11614913": {
        "gene": "MIR196A2",
        "category": "disease",
        "title": "microRNA Cancer Risk",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal microRNA function."},
            "CT": {
                "effect": "variant",
                "description": "Different microRNA ekspresyonu.",
            },
            "CC": {
                "effect": "altered",
                "description": "Altered gene regulation. Risk factor for some cancer types.",
            },
        },
        "frequency": "~30%",
    },
    # ================================================================
    # FOOD - Nutrition and metabolism
    # ================================================================
    "rs4988235": {
        "gene": "LCT",
        "category": "food",
        "title": "Lactose Tolerance",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "intolerant",
                "description": "Lactose intolerance likely. Dairy products may cause digestive problems.",
            },
            "AG": {
                "effect": "tolerant",
                "description": "You have lactose tolerance. You can digest dairy products.",
            },
            "GG": {
                "effect": "tolerant",
                "description": "Full lactose tolerance. You produce the enzyme necessary for milk digestion in adulthood.",
            },
        },
        "frequency": "~35% worldwide (tolerant)",
    },
    "rs1801282": {
        "gene": "PPARG",
        "category": "food",
        "title": "Fat Metabolism",
        "risk_allele": "G",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "Normal fat metabolism. Standard diet suitable.",
            },
            "CG": {
                "effect": "efficient",
                "description": "More efficient fat metabolism. Low from low-fat diets more you may benefit.",
            },
            "GG": {
                "effect": "very_efficient",
                "description": "Very efficient fat storage. Controlling fat intake important.",
            },
        },
        "frequency": "~15% (G alleli)",
    },
    "rs762551": {
        "gene": "CYP1A2",
        "category": "food",
        "title": "Caffeine Metabolism",
        "risk_allele": "C",
        "variants": {
            "AA": {
                "effect": "fast",
                "description": "Fast caffeine metabolism! Coffee is processed quickly, you can consume more.",
            },
            "AC": {
                "effect": "moderate",
                "description": "Moderate speed caffeine metabolism.",
            },
            "CC": {
                "effect": "slow",
                "description": "Slow caffeine metabolism. Caffeine may disrupt your sleep late at night. Limit to 1-2 cups per day.",
            },
        },
        "frequency": "~45% (AA)",
    },
    "rs1726866": {
        "gene": "TAS2R38",
        "category": "food",
        "title": "Bitter Taste Perception (PTC)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "non_taster",
                "description": '"Non-taster": You perceive bitter tastes less. Broccoli and Brussels sprouts taste less bitter to you.',
            },
            "CT": {
                "effect": "medium",
                "description": "Moderate bitter taste perception.",
            },
            "TT": {
                "effect": "super_taster",
                "description": '"Super taster"! You perceive bitter tastes intensely. Green vegetables and coffee may taste very bitter.',
            },
        },
        "frequency": "~25% (TT)",
    },
    "rs671": {
        "gene": "ALDH2",
        "category": "food",
        "title": "Alcohol Metabolism",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal alcohol metabolism."},
            "AG": {
                "effect": "reduced",
                "description": 'Reduced ALDH2 activity. Facial flushing after alcohol ("Asian flush") may occur.',
            },
            "AA": {
                "effect": "deficient",
                "description": "ALDH2 deficiency. Alcohol consumption may be very uncomfortable and carries health risks.",
            },
        },
        "frequency": "~30% (East Asia), <5% (Europe)",
    },
    "rs9939609": {
        "gene": "FTO",
        "category": "food",
        "title": "Obesity Predisposition (FTO)",
        "risk_allele": "A",
        "variants": {
            "TT": {
                "effect": "normal",
                "description": "Low obezite riski. Normal hunger/satiety signals.",
            },
            "AT": {
                "effect": "moderate",
                "description": "Moderate obezite riski. Portion control beneficial.",
            },
            "AA": {
                "effect": "increased",
                "description": "Increased obezite riski (~3kg extra). Hunger hormone ghrelin may be high. Protein-rich diet recommended.",
            },
        },
        "frequency": "~16% (AA)",
    },
    "rs1799883": {
        "gene": "FABP2",
        "category": "food",
        "title": "Fat Absorption",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal fat absorption."},
            "AG": {
                "effect": "increased",
                "description": "Increased fat absorption. Be careful with fatty foods.",
            },
            "GG": {
                "effect": "high",
                "description": "High fat absorption. Limit saturated fat intake.",
            },
        },
        "frequency": "~30% (G alleli)",
    },
    "rs1801394": {
        "gene": "MTRR",
        "category": "food",
        "title": "B12 Vitamin Metabolism",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal B12 metabolism."},
            "AG": {
                "effect": "reduced",
                "description": "Reduced methionine synthase reductase activity. B12 supplementation may be beneficial.",
            },
            "GG": {
                "effect": "significantly_reduced",
                "description": "Significant reduced aktivite. Methylcobalamin form recommended.",
            },
        },
        "frequency": "~25%",
    },
    "rs602662": {
        "gene": "FUT2",
        "category": "food",
        "title": "B12 Absorption (Secretor Status)",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "secretor",
                "description": "Secretor genotype. Normal B12 absorption.",
            },
            "AG": {
                "effect": "moderate",
                "description": "Heterozigot. Normal B12 absorption.",
            },
            "AA": {
                "effect": "non_secretor",
                "description": "Non-secretor. Reduced B12 emilimi. Probiotics and fermented foods beneficial.",
            },
        },
        "frequency": "~20% (non-secretor)",
    },
    "rs7501331": {
        "gene": "BCMO1",
        "category": "food",
        "title": "Beta-Carotene Conversion",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "efficient",
                "description": "Efficient beta-carotene → vitamin A conversion.",
            },
            "CT": {
                "effect": "reduced",
                "description": "Reduced conversion. More consume carrots and sweet potatoes.",
            },
            "TT": {
                "effect": "poor",
                "description": "Poor beta-karoten conversion. Prefer preformed vitamin A (liver, eggs).",
            },
        },
        "frequency": "~40%",
    },
    "rs12934922": {
        "gene": "BCMO1",
        "category": "food",
        "title": "Vitamin A Metabolism",
        "risk_allele": "T",
        "variants": {
            "AA": {
                "effect": "efficient",
                "description": "Efficient A vitamini conversion.",
            },
            "AT": {
                "effect": "reduced",
                "description": "Reduced conversion kapasitesi.",
            },
            "TT": {
                "effect": "poor",
                "description": "Low beta-karoten conversion. Animal vitamin A sources recommended.",
            },
        },
        "frequency": "~25%",
    },
    "rs4654748": {
        "gene": "NBPF3",
        "category": "food",
        "title": "B6 Vitamin Level",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal B6 levels."},
            "CT": {"effect": "lower", "description": "Lower B6 seviyeleri may be."},
            "TT": {
                "effect": "low",
                "description": "Low B6 seviyeleri. B6-rich foods or supplementation recommended.",
            },
        },
        "frequency": "~30%",
    },
    "rs2282679": {
        "gene": "GC",
        "category": "food",
        "title": "Vitamin D Binding Protein",
        "risk_allele": "C",
        "variants": {
            "AA": {
                "effect": "normal",
                "description": "Normal vitamin D transport capacity.",
            },
            "AC": {
                "effect": "reduced",
                "description": "Reduced vitamin D transport. Sun or supplementation recommended.",
            },
            "CC": {
                "effect": "low",
                "description": "Low D vitamini seviyeleri riski. D3 supplementation recommended.",
            },
        },
        "frequency": "~30%",
    },
    "rs10741657": {
        "gene": "CYP2R1",
        "category": "food",
        "title": "Vitamin D Activation",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal vitamin D activation."},
            "AG": {
                "effect": "reduced",
                "description": "Reduced D vitamini aktivasyonu.",
            },
            "AA": {
                "effect": "low",
                "description": "Low D vitamini aktivasyonu. High doz takviye gerekebilir.",
            },
        },
        "frequency": "~20%",
    },
    "rs2070895": {
        "gene": "LIPC",
        "category": "food",
        "title": "HDL (Good) Cholesterol",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal HDL seviyeleri."},
            "AG": {"effect": "elevated", "description": "High HDL seviyeleri."},
            "AA": {
                "effect": "high_hdl",
                "description": "Very high HDL seviyeleri! Cardiovascular protection.",
            },
        },
        "frequency": "~25%",
    },
    "rs5082": {
        "gene": "APOA2",
        "category": "food",
        "title": "Saturated Fat Sensitivity",
        "risk_allele": "C",
        "variants": {
            "TT": {
                "effect": "resistant",
                "description": "Less sensitive to saturated fat. High you are less affected by high-fat diets.",
            },
            "CT": {
                "effect": "moderate",
                "description": "Moderate saturated fat sensitivity.",
            },
            "CC": {
                "effect": "sensitive",
                "description": "Sensitive to saturated fat! High risk of weight gain increases with high saturated fat intake.",
            },
        },
        "frequency": "~15%",
    },
    "rs1695": {
        "gene": "GSTP1",
        "category": "food",
        "title": "Detoksifikasyon (Glutatyon)",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "normal",
                "description": "Normal glutatyon transferaz activity.",
            },
            "AG": {
                "effect": "reduced",
                "description": "Reduced detoksifikasyon kapasitesi.",
            },
            "GG": {
                "effect": "low",
                "description": "Low detoksifikasyon kapasitesi. Cruciferous vegetables (broccoli, cauliflower) recommended.",
            },
        },
        "frequency": "~25%",
    },
    # ================================================================
    # FITNESS - Physical performance
    # ================================================================
    "rs1815739": {
        "gene": "ACTN3",
        "category": "fitness",
        "title": "Muscle Type (Sprinter vs Endurance)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "power",
                "description": '"Sprinter" genotype! Fast-twitch muscle fibers dominant. Advantageous in explosive power sports (sprint, weightlifting).',
            },
            "CT": {
                "effect": "mixed",
                "description": "Mixed kas tipi. You are good at both power and endurance sports.",
            },
            "TT": {
                "effect": "endurance",
                "description": '"Endurance" genotype. Slow-twitch muscle fibers dominant. Advantageous in long-duration sports like marathon, cycling.',
            },
        },
        "frequency": "~20% (TT)",
    },
    "rs8192678": {
        "gene": "PPARGC1A",
        "category": "fitness",
        "title": "Aerobik Kapasite (PGC-1α)",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal aerobik kapasite."},
            "AG": {
                "effect": "enhanced",
                "description": "Increased aerobik kapasite potansiyeli.",
            },
            "AA": {
                "effect": "high",
                "description": "High aerobik kapasite potansiyeli! Strong mitochondrial production and energy metabolism.",
            },
        },
        "frequency": "~35% (A alleli)",
    },
    "rs1042713": {
        "gene": "ADRB2",
        "category": "fitness",
        "title": "Exercise Efficiency",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal exercise response."},
            "AG": {"effect": "good", "description": "Good exercise response."},
            "GG": {
                "effect": "enhanced",
                "description": "Increased exercise efficiency! You will benefit more from cardiovascular exercise.",
            },
        },
        "frequency": "~40% (GG)",
    },
    "rs4253778": {
        "gene": "PPARA",
        "category": "fitness",
        "title": "Fat Burning",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal fat burning."},
            "GC": {
                "effect": "enhanced",
                "description": "Increased fat burning capacity.",
            },
            "CC": {
                "effect": "high",
                "description": "High fat burning capacity! You efficiently use fat as energy during long-duration exercise.",
            },
        },
        "frequency": "~15% (C alleli)",
    },
    "rs1800169": {
        "gene": "CNTF",
        "category": "fitness",
        "title": "Muscle Strength Potential",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal muscle strength potential.",
            },
            "AG": {
                "effect": "moderate",
                "description": "Moderately increased muscle strength potential.",
            },
            "AA": {
                "effect": "enhanced",
                "description": "Increased muscle strength potential! from strength training more you may benefit.",
            },
        },
        "frequency": "~20% (A alleli)",
    },
    "rs2016520": {
        "gene": "PPARD",
        "category": "fitness",
        "title": "Endurance Capacity",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal endurance capacity."},
            "TC": {
                "effect": "enhanced",
                "description": "Increased endurance capacity.",
            },
            "CC": {
                "effect": "high",
                "description": "High endurance capacity! You are advantageous in long-duration exercises.",
            },
        },
        "frequency": "~20% (CC)",
    },
    "rs7181866": {
        "gene": "AGT",
        "category": "fitness",
        "title": "Power vs Endurance",
        "risk_allele": "C",
        "variants": {
            "TT": {
                "effect": "endurance",
                "description": "Predisposed to endurance sports.",
            },
            "CT": {"effect": "mixed", "description": "Mixed performans profili."},
            "CC": {
                "effect": "power",
                "description": "Predisposed to power sports! Advantageous in short-duration intense activities.",
            },
        },
        "frequency": "~40%",
    },
    "rs699": {
        "gene": "AGT",
        "category": "fitness",
        "title": "Anjiyotensinojen (M235T)",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "endurance",
                "description": "Endurance advantage. Low blood pressure tendency.",
            },
            "AG": {"effect": "mixed", "description": "Mixed profil."},
            "GG": {
                "effect": "power",
                "description": "Power advantage. High blood pressure risk should be monitored.",
            },
        },
        "frequency": "~40%",
    },
    "rs1799752": {
        "gene": "ACE",
        "category": "fitness",
        "title": "ACE I/D - Endurance vs Power",
        "risk_allele": "D",
        "variants": {
            "II": {
                "effect": "endurance",
                "description": "Endurance genotype! Advantageous for marathon, swimming, cycling.",
            },
            "ID": {
                "effect": "mixed",
                "description": "Mixed genotype. Very versatile athletic potential.",
            },
            "DD": {
                "effect": "power",
                "description": "Power genotype! Advantageous for sprint, weightlifting, wrestling.",
            },
        },
        "frequency": "Her genotype ~%25-35",
    },
    "rs1050450": {
        "gene": "GPX1",
        "category": "fitness",
        "title": "Antioksidan Kapasite",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal antioxidant capacity."},
            "CT": {
                "effect": "reduced",
                "description": "Reduced antioxidant capacity. Antioxidant foods recommended.",
            },
            "TT": {
                "effect": "low",
                "description": "Low antioxidant capacity. Selenium and antioxidants important.",
            },
        },
        "frequency": "~25%",
    },
    "rs4880": {
        "gene": "SOD2",
        "category": "fitness",
        "title": "Superoxide Dismutase (MnSOD)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "efficient",
                "description": "Efficient mitokondriyal antioksidan.",
            },
            "CT": {
                "effect": "moderate",
                "description": "Moderate antioksidan activity.",
            },
            "TT": {
                "effect": "less_efficient",
                "description": "Less efficient antioxidant. Recovery after exercise may be slow.",
            },
        },
        "frequency": "~25%",
    },
    "rs2228570": {
        "gene": "VDR",
        "category": "fitness",
        "title": "Vitamin D Receptor (Muscle Function)",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal vitamin D receptor function.",
            },
            "AG": {"effect": "variant", "description": "Different vitamin D response."},
            "AA": {
                "effect": "altered",
                "description": "Altered muscle function response. Adequate vitamin D is important.",
            },
        },
        "frequency": "~35%",
    },
    "rs11549465": {
        "gene": "HIF1A",
        "category": "fitness",
        "title": "Altitude Adaptation",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal oxygen adaptation."},
            "CT": {
                "effect": "enhanced",
                "description": "Increased hypoxia adaptation.",
            },
            "TT": {
                "effect": "superior",
                "description": "Superior altitude adaptation! Advantageous in altitude training.",
            },
        },
        "frequency": "~10%",
    },
    # ================================================================
    # COGNITIVE - Cognitive traits
    # ================================================================
    "rs9536314": {
        "gene": "KIBRA",
        "category": "cognitive",
        "title": "Memory Capacity",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal memory capacity."},
            "CT": {"effect": "enhanced", "description": "Increased memory capacity."},
            "TT": {
                "effect": "superior",
                "description": "Superior episodic memory capacity! You remember events and experiences better.",
            },
        },
        "frequency": "~25% (T alleli)",
    },
    "rs363050": {
        "gene": "SNAP25",
        "category": "cognitive",
        "title": "Attention and Concentration",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal attention capacity."},
            "AG": {
                "effect": "enhanced",
                "description": "Increased attention capacity.",
            },
            "GG": {
                "effect": "superior",
                "description": "Superior attention and concentration capacity! Strong synaptic transmission.",
            },
        },
        "frequency": "~30% (GG)",
    },
    "rs17070145": {
        "gene": "WWC1",
        "category": "cognitive",
        "title": "Long-Term Memory",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal long-term memory."},
            "CT": {
                "effect": "enhanced",
                "description": "Increased long-term memory capacity.",
            },
            "TT": {
                "effect": "superior",
                "description": "Superior long-term memory! You retain learned information for a long time.",
            },
        },
        "frequency": "~25% (T alleli)",
    },
    "rs1018381": {
        "gene": "DTNBP1",
        "category": "cognitive",
        "title": "Working Memory",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "Normal working memory capacity.",
            },
            "CT": {"effect": "enhanced", "description": "Increased working memory."},
            "TT": {
                "effect": "high",
                "description": "High working memory capacity! multiple tasks and advantageous in problem solving.",
            },
        },
        "frequency": "~20% (TT)",
    },
    "rs10119": {
        "gene": "APOE",
        "category": "cognitive",
        "title": "Cognitive Aging",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal cognitive aging."},
            "AG": {
                "effect": "protected",
                "description": "Protection against cognitive aging.",
            },
            "GG": {
                "effect": "highly_protected",
                "description": "High cognitive protection. Maintaining mental sharpness with age.",
            },
        },
        "frequency": "~15%",
    },
    "rs6994992": {
        "gene": "NRG1",
        "category": "cognitive",
        "title": "Creative Thinking",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal cognitive processing."},
            "CT": {
                "effect": "creative",
                "description": "Increased creative thinking potential.",
            },
            "TT": {
                "effect": "highly_creative",
                "description": "High creativity potential! different thinking and problem solving.",
            },
        },
        "frequency": "~20%",
    },
    "rs1800544": {
        "gene": "ADRA2A",
        "category": "cognitive",
        "title": "Focus and Attention",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal attention function."},
            "CG": {"effect": "enhanced", "description": "Increased focus capacity."},
            "CC": {
                "effect": "superior",
                "description": "Superior focus! Advantageous in tasks requiring long-term concentration.",
            },
        },
        "frequency": "~20%",
    },
    "rs4570625": {
        "gene": "TPH2",
        "category": "cognitive",
        "title": "Emotional Intelligence",
        "risk_allele": "T",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal emotional processing."},
            "GT": {
                "effect": "sensitive",
                "description": "More sensitive emotional processing.",
            },
            "TT": {
                "effect": "highly_sensitive",
                "description": "High emotional sensitivity. Associated with empathy and emotional intelligence.",
            },
        },
        "frequency": "~15%",
    },
    "rs2268498": {
        "gene": "OXTR",
        "category": "cognitive",
        "title": "Social Cognition",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal social cognition."},
            "CT": {"effect": "enhanced", "description": "Increased social cognition."},
            "CC": {
                "effect": "superior",
                "description": "Superior social cognition! Advantageous in reading facial expressions and social cues.",
            },
        },
        "frequency": "~25%",
    },
    # ================================================================
    # LIFESTYLE - Lifestyle
    # ================================================================
    "rs1801260": {
        "gene": "CLOCK",
        "category": "lifestyle",
        "title": "Circadian Rhythm (Morning/Evening)",
        "risk_allele": "C",
        "variants": {
            "AA": {
                "effect": "morning",
                "description": '"Morning person" genotype! You are predisposed to waking early and being productive in morning hours.',
            },
            "AG": {
                "effect": "flexible",
                "description": "Flexible circadian rhythm. You may adapt to both time periods.",
            },
            "GG": {
                "effect": "evening",
                "description": '"Night owl" genotype! You may be more productive late at night.',
            },
        },
        "frequency": "~30% her genotype",
    },
    "rs57875989": {
        "gene": "DEC2",
        "category": "lifestyle",
        "title": "Short Sleep Gene",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "normal", "description": "Normal sleep need (7-8 hours)."},
            "AG": {
                "effect": "reduced",
                "description": "Reduced sleep need. 6-7 hours yeterli may be.",
            },
            "GG": {
                "effect": "short_sleeper",
                "description": '"Short sleeper" genotype! You may be functional with 4-6 hours of sleep. Very rare variant.',
            },
        },
        "frequency": "<1% (GG)",
    },
    "rs1799971": {
        "gene": "OPRM1",
        "category": "lifestyle",
        "title": "Reward System Response",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "normal",
                "description": "Normal opioid receptor activity.",
            },
            "AG": {
                "effect": "altered",
                "description": "Altered opioid receptor activity. Difference in reward system.",
            },
            "GG": {
                "effect": "variant",
                "description": "Different reward system response. You may be less affected by social connections.",
            },
        },
        "frequency": "~15% (G alleli)",
    },
    "rs73598374": {
        "gene": "ADA",
        "category": "lifestyle",
        "title": "Derin Uyku Kalitesi",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal deep sleep quality."},
            "AG": {
                "effect": "enhanced",
                "description": "Increased deep sleep quality.",
            },
            "AA": {
                "effect": "superior",
                "description": "Superior deep sleep quality! You recover better during sleep.",
            },
        },
        "frequency": "~10% (A alleli)",
    },
    "rs2278749": {
        "gene": "PER2",
        "category": "lifestyle",
        "title": "Sleep Pattern",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal circadian pattern."},
            "CT": {
                "effect": "sensitive",
                "description": "More sensitive to light changes.",
            },
            "TT": {
                "effect": "highly_sensitive",
                "description": "Very sensitive to circadian rhythm. Regular sleep routine is very important.",
            },
        },
        "frequency": "~20%",
    },
    "rs324650": {
        "gene": "MTNR1B",
        "category": "lifestyle",
        "title": "Melatonin Receptor",
        "risk_allele": "G",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal melatonin response."},
            "GT": {
                "effect": "variant",
                "description": "Different melatonin receptor activity.",
            },
            "GG": {
                "effect": "altered",
                "description": "Altered melatonin response. Sleep hygiene and dark environment are important.",
            },
        },
        "frequency": "~30%",
    },
    "rs10830963": {
        "gene": "MTNR1B",
        "category": "lifestyle",
        "title": "Night Eating Tendency",
        "risk_allele": "G",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal evening metabolism."},
            "CG": {
                "effect": "risk",
                "description": "Late eating may affect metabolism.",
            },
            "GG": {
                "effect": "high_risk",
                "description": "Late eating may increase Type 2 diabetes risk. Early evening meal recommended.",
            },
        },
        "frequency": "~30%",
    },
    "rs228697": {
        "gene": "PER3",
        "category": "lifestyle",
        "title": "Sleep Need",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Standart sleep need."},
            "CG": {
                "effect": "higher",
                "description": "Higher sleep need may be present.",
            },
            "CC": {
                "effect": "high",
                "description": "High sleep need. 8+ hours of sleep may be required for optimal performance.",
            },
        },
        "frequency": "~25%",
    },
    # ================================================================
    # LONGEVITY - Longevity and aging
    # ================================================================
    "rs2802292": {
        "gene": "FOXO3",
        "category": "longevity",
        "title": "Longevity Gene (FOXO3)",
        "risk_allele": "G",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal life expectancy."},
            "GT": {
                "effect": "longevity",
                "description": "Longevity-associated variant carrier.",
            },
            "GG": {
                "effect": "centenarian",
                "description": "Variant strongly associated with living past 100! Increased cellular stress resistance.",
            },
        },
        "frequency": "~25% (G alleli)",
    },
    "rs1042714": {
        "gene": "ADRB2",
        "category": "longevity",
        "title": "Metabolic Health",
        "risk_allele": "C",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal metabolik profil."},
            "CG": {"effect": "efficient", "description": "More efficient metabolizma."},
            "CC": {
                "effect": "longevity",
                "description": "Longevity-associated metabolic profile.",
            },
        },
        "frequency": "~15%",
    },
    "rs3758391": {
        "gene": "SIRT1",
        "category": "longevity",
        "title": "Sirtuin 1 (Aging Regulator)",
        "risk_allele": "C",
        "variants": {
            "TT": {"effect": "normal", "description": "Normal SIRT1 activity."},
            "CT": {
                "effect": "enhanced",
                "description": "Increased SIRT1 activity. Increased cellular repair.",
            },
            "CC": {
                "effect": "longevity",
                "description": "High SIRT1 activity! Associated with healthy aging and longevity.",
            },
        },
        "frequency": "~20%",
    },
    "rs13150703": {
        "gene": "TERT",
        "category": "longevity",
        "title": "Telomerase (Telomere Length)",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal telomeraz activity."},
            "AG": {
                "effect": "enhanced",
                "description": "Increased telomeraz activity.",
            },
            "AA": {
                "effect": "longevity",
                "description": "High telomerase activity! Longer telomeres and slow cellular aging.",
            },
        },
        "frequency": "~15%",
    },
    "rs2075650": {
        "gene": "TOMM40",
        "category": "longevity",
        "title": "Mitokondriyal Fonksiyon",
        "risk_allele": "A",
        "variants": {
            "GG": {
                "effect": "normal",
                "description": "Normal mitokondriyal fonksiyon.",
            },
            "AG": {
                "effect": "variant",
                "description": "Different mitokondriyal fonksiyon.",
            },
            "AA": {
                "effect": "efficient",
                "description": "Efficient mitokondriyal fonksiyon. Enerji production optimize.",
            },
        },
        "frequency": "~20%",
    },
    # ================================================================
    # IMMUNITY - Immune system
    # ================================================================
    "rs333": {
        "gene": "CCR5",
        "category": "immunity",
        "title": "HIV Direnci (CCR5-delta32)",
        "risk_allele": "D",
        "variants": {
            "WW": {"effect": "normal", "description": "Normal CCR5 receptor."},
            "WD": {
                "effect": "resistant",
                "description": "Partial HIV resistance. Disease progression is slow.",
            },
            "DD": {
                "effect": "immune",
                "description": "Complete HIV immunity! CCR5 receptor is missing. 1% in Northwest Europe.",
            },
        },
        "frequency": "~10% (Europe carrier)",
    },
    "rs8176719": {
        "gene": "ABO",
        "category": "immunity",
        "title": "Blood Type O",
        "risk_allele": "delG",
        "variants": {
            "GG": {"effect": "A_or_B", "description": "A or B blood type."},
            "G-": {"effect": "carrier", "description": "O blood type carrier."},
            "--": {
                "effect": "O_type",
                "description": "O blood type! Protection against some infections, but predisposition to some diseases.",
            },
        },
        "frequency": "~40% (O type)",
    },
    "rs1800896": {
        "gene": "IL10",
        "category": "immunity",
        "title": "Anti-inflammatory Response (IL-10)",
        "risk_allele": "G",
        "variants": {
            "AA": {
                "effect": "low",
                "description": "Low IL-10 production. High inflammation tendency.",
            },
            "AG": {"effect": "moderate", "description": "Moderate IL-10 production."},
            "GG": {
                "effect": "high",
                "description": "High IL-10 production! Strong anti-inflammatory response.",
            },
        },
        "frequency": "~30%",
    },
    "rs1800795": {
        "gene": "IL6",
        "category": "immunity",
        "title": "Inflammation Response (IL-6)",
        "risk_allele": "G",
        "variants": {
            "CC": {
                "effect": "low_inflammation",
                "description": "Low IL-6 production. Low inflammation tendency.",
            },
            "CG": {"effect": "moderate", "description": "Moderate IL-6 production."},
            "GG": {
                "effect": "high_inflammation",
                "description": "High IL-6 production. Chronic inflammation risk. Anti-inflammatory diet beneficial.",
            },
        },
        "frequency": "~35%",
    },
    "rs1800629": {
        "gene": "TNF",
        "category": "immunity",
        "title": "TNF-alpha Production",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal TNF-alpha production."},
            "AG": {
                "effect": "elevated",
                "description": "Increased TNF-alpha production. Inflammation tendency.",
            },
            "AA": {
                "effect": "high",
                "description": "High TNF-alpha production. Autoimmune disease risk may be increased.",
            },
        },
        "frequency": "~15%",
    },
    "rs1800797": {
        "gene": "IL6",
        "category": "immunity",
        "title": "Immune Response Strength",
        "risk_allele": "G",
        "variants": {
            "AA": {"effect": "moderate", "description": "Moderate immune response."},
            "AG": {"effect": "enhanced", "description": "Increased immune response."},
            "GG": {
                "effect": "strong",
                "description": "Strong immune response! Faster response to infections.",
            },
        },
        "frequency": "~40%",
    },
    "rs1143634": {
        "gene": "IL1B",
        "category": "immunity",
        "title": "Acute Inflammation (IL-1β)",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal IL-1β response."},
            "CT": {
                "effect": "enhanced",
                "description": "Increased akut inflammation response.",
            },
            "TT": {
                "effect": "high",
                "description": "High akut inflammation response. Strong response to infections.",
            },
        },
        "frequency": "~25%",
    },
    "rs2243250": {
        "gene": "IL4",
        "category": "immunity",
        "title": "Allergy Tendency (IL-4)",
        "risk_allele": "T",
        "variants": {
            "CC": {
                "effect": "normal",
                "description": "Normal IL-4 production. Low alerji riski.",
            },
            "CT": {
                "effect": "elevated",
                "description": "Increased IL-4 production. Alerji tendency.",
            },
            "TT": {
                "effect": "high",
                "description": "High IL-4 production. Allergy, asthma and atopic disease risk increased.",
            },
        },
        "frequency": "~15%",
    },
    # ================================================================
    # INTERESTING - Markers for interesting combinations
    # ================================================================
    "rs1805009": {
        "gene": "MC1R",
        "category": "interesting",
        "title": "MC1R Varyant (D294H)",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Common MC1R variant."},
            "AG": {"effect": "carrier", "description": "MC1R D294H carrier."},
            "AA": {
                "effect": "variant",
                "description": "Rare MC1R variant. May affect hair and skin color.",
            },
        },
        "frequency": "~5%",
    },
    "rs4778138": {
        "gene": "OCA2",
        "category": "interesting",
        "title": "Eye Color Modifiye Edici",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Standart pigmentasyon."},
            "AG": {
                "effect": "modifier",
                "description": "Tendency toward lightness in eye color.",
            },
            "AA": {
                "effect": "light",
                "description": "Variant associated with light eye color.",
            },
        },
        "frequency": "~15%",
    },
    "rs1805006": {
        "gene": "MC1R",
        "category": "interesting",
        "title": "MC1R D84E Variant",
        "risk_allele": "A",
        "variants": {
            "GG": {"effect": "normal", "description": "Normal MC1R."},
            "AG": {
                "effect": "carrier",
                "description": "D84E carrier. Tendency toward light skin and hair.",
            },
            "AA": {
                "effect": "variant",
                "description": "Rare D84E variant. In the red hair spectrum.",
            },
        },
        "frequency": "~2%",
    },
    "rs2733832": {
        "gene": "TYR",
        "category": "interesting",
        "title": "Pigmentasyon Variant",
        "risk_allele": "T",
        "variants": {
            "CC": {"effect": "normal", "description": "Normal melanin production."},
            "CT": {"effect": "light", "description": "Slightly light pigmentation."},
            "TT": {
                "effect": "very_light",
                "description": "Very light pigmentation tendency.",
            },
        },
        "frequency": "~10%",
    },
}


def get_snp_info(rsid):
    """Get SNP information from database"""
    return SNP_DATABASE.get(rsid.lower(), None)


def get_snps_by_category(category):
    """Get all SNPs in a specific category"""
    return {
        rsid: info
        for rsid, info in SNP_DATABASE.items()
        if info.get("category") == category
    }


def get_all_rsids():
    """Return all rsids in the database"""
    return list(SNP_DATABASE.keys())


def get_category_counts():
    """Return the count of SNPs in each category"""
    counts = {}
    for snp in SNP_DATABASE.values():
        cat = snp.get("category", "unknown")
        counts[cat] = counts.get(cat, 0) + 1
    return counts
