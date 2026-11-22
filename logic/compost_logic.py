"""C:N mixture calculations and compost planning suggestions."""

from data.materials import MATERIALS, COMPOST_PROPERTIES, TARGET_CN_RATIO


def calculate_cn_ratio(entries):
    """Calculate a mixture C:N ratio using Cornell's wet-weight equation.

    For each material:
        carbon contribution = Q * C * (100 - M)
        nitrogen contribution = Q * N * (100 - M)

    Q is wet mass, C and N are dry-basis percentages, and M is
    moisture percentage on a wet-weight basis. The common percentage
    divisors cancel when total carbon is divided by total nitrogen.
    """
    total_carbon = 0.0
    total_nitrogen = 0.0
    details = []
    missing_data = []

    for material, quantity in entries:
        if quantity <= 0 or MATERIALS[material][0] == "Unsuitable":
            continue

        properties = COMPOST_PROPERTIES.get(material)
        if not properties or properties.get("moisture") is None:
            missing_data.append(material)
            continue

        nitrogen_pct = properties["nitrogen"]
        material_cn = properties["cn_ratio"]
        moisture_pct = properties["moisture"]
        carbon_pct = nitrogen_pct * material_cn
        dry_fraction = (100 - moisture_pct) / 100

        carbon_contribution = quantity * dry_fraction * carbon_pct / 100
        nitrogen_contribution = quantity * dry_fraction * nitrogen_pct / 100

        total_carbon += carbon_contribution
        total_nitrogen += nitrogen_contribution
        details.append({
            "material": material,
            "quantity": quantity,
            "carbon_pct": carbon_pct,
            "nitrogen_pct": nitrogen_pct,
            "moisture_pct": moisture_pct,
            "material_cn": material_cn,
            "carbon_mass": carbon_contribution,
            "nitrogen_mass": nitrogen_contribution,
            "source": properties["source"],
        })

    if missing_data or total_nitrogen <= 0:
        return None, total_carbon, total_nitrogen, details, missing_data

    return total_carbon / total_nitrogen, total_carbon, total_nitrogen, details, missing_data


def make_recommendations(entries):
    green = sum(q for m, q in entries if q > 0 and MATERIALS[m][0] == "Green")
    brown = sum(q for m, q in entries if q > 0 and MATERIALS[m][0] == "Brown")
    unsuitable = [m for m, q in entries if q > 0 and MATERIALS[m][0] == "Unsuitable"]
    cn_ratio, carbon_mass, nitrogen_mass, details, missing_data = calculate_cn_ratio(entries)
    tips = []

    if unsuitable:
        tips.append("Remove unsuitable materials: " + ", ".join(unsuitable) + ".")

    if missing_data:
        tips.append(
            "A complete published moisture value is not available for "
            + ", ".join(missing_data)
            + ". The C:N estimate is not shown for this mixture. Remove these materials or use a measured moisture value before calculating."
        )
    elif cn_ratio is None:
        tips.append("Enter a positive quantity of at least one suitable material with complete reference data.")
    elif cn_ratio < TARGET_CN_RATIO:
        tips.append(
            "The estimated C:N ratio is below the approximate 30:1 starting target. "
            "Consider adding a carbon-rich material, such as dry leaves or plain shredded cardboard."
        )
    elif cn_ratio > TARGET_CN_RATIO:
        tips.append(
            "The estimated C:N ratio is above the approximate 30:1 starting target. "
            "Consider adding a nitrogen-rich material, such as vegetable scraps or fresh grass clippings."
        )
    else:
        tips.append("The estimated C:N ratio is approximately 30:1, which matches the general starting guideline.")

    tips.append("This result is an estimate from typical reference data. Actual material composition and nutrient availability can vary.")
    return green, brown, unsuitable, tips, cn_ratio, carbon_mass, nitrogen_mass, details, missing_data
