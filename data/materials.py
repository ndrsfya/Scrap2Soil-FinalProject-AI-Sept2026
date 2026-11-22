"""Material categories and published compost reference data."""

MATERIALS = {
    "Fruit peels": ("Green", "Fruit waste reference values are used as an estimate."),
    "Vegetable scraps": ("Green", "Nitrogen-rich kitchen material. Chop into smaller pieces."),
    "Coffee grounds": ("Green", "Mix with other materials rather than adding in thick layers."),
    "Fresh grass clippings": ("Green", "Add in thin layers to reduce compaction."),
    "Dry leaves": ("Brown", "Carbon-rich material that helps absorb moisture."),
    "Shredded cardboard": ("Brown", "Use plain, uncoated cardboard cut into small pieces."),
    "Dry twigs": ("Brown", "Can improve airflow, but a complete moisture reference is not available."),
    "Straw": ("Brown", "Wheat straw values are used as a reference."),
    "Plastic": ("Unsuitable", "Do not add plastic to compost."),
    "Glass": ("Unsuitable", "Do not add glass to compost."),
    "Metal": ("Unsuitable", "Do not add metal to compost."),
    "Meat and fish": ("Unsuitable", "Not included in this beginner composting plan."),
    "Dairy products": ("Unsuitable", "Not included in this beginner composting plan."),
}

# Percentages are on a dry-matter basis for nitrogen and carbon, and on a
# wet-weight basis for moisture. Carbon is calculated as N (%) x C:N ratio.
# A missing value means there is not enough matching reference data to
# calculate that material reliably using the Cornell wet-weight equation.
COMPOST_PROPERTIES = {
    "Fruit peels": {
        "nitrogen": 1.4,
        "cn_ratio": 40,
        "moisture": 80,
        "source": "Cornell On-Farm Composting Handbook, fruit wastes (average)",
    },
    "Vegetable scraps": {
        "nitrogen": 2.7,
        "cn_ratio": 19,
        "moisture": 87,
        "source": "Cornell On-Farm Composting Handbook, vegetable produce",
    },
    "Coffee grounds": {
        "nitrogen": 2.34,
        "cn_ratio": 22.7,
        "moisture": 66.4,
        "source": "Spent coffee grounds feedstock study",
    },
    "Fresh grass clippings": {
        "nitrogen": 3.4,
        "cn_ratio": 17,
        "moisture": 82,
        "source": "Cornell On-Farm Composting Handbook, grass clippings (average)",
    },
    "Dry leaves": {
        "nitrogen": 0.9,
        "cn_ratio": 54,
        "moisture": 38,
        "source": "Cornell On-Farm Composting Handbook, leaves (average)",
    },
    "Shredded cardboard": {
        "nitrogen": 0.10,
        "cn_ratio": 563,
        "moisture": 8,
        "source": "Cornell On-Farm Composting Handbook, corrugated cardboard",
    },
    "Dry twigs": {
        "nitrogen": 0.09,
        "cn_ratio": 560,
        "moisture": None,
        "source": "Cornell hardwood chips and shavings (proxy); moisture not reported",
    },
    "Straw": {
        "nitrogen": 0.3,
        "cn_ratio": 128,
        "moisture": 15,
        "source": "Cornell Field Guide to On-Farm Composting, wheat straw example",
    },
}

GREEN = "#6F9878"
DARK_GREEN = "#294B34"
PALE_GREEN = "#E4EEE1"
SOFT_GREEN = "#FBF8F0"
TEXT = "#26352A"

TARGET_CN_RATIO = 30
