"""Compost mixture planning screen."""

from datetime import date

import streamlit as st

from data.materials import MATERIALS, COMPOST_PROPERTIES, TARGET_CN_RATIO
from logic.compost_logic import make_recommendations
from ui.components import page_heading, green_table


def render_planner():
    page_heading(
        "PLAN YOUR MIXTURE",
        "Compost Planner",
        "Choose your materials and enter the amount of each one in kilograms."
    )

    st.markdown(
        '<div class="green-note">The planner estimates the mixture C:N ratio using wet weight, '
        'reference carbon and nitrogen percentages, and moisture content. Cornell describes '
        'approximately 30:1 as a usual starting guideline.</div>',
        unsafe_allow_html=True,
    )

    with st.form("planner_form"):
        batch_name = st.text_input("Batch name", placeholder="e.g. Cafeteria food waste")
        start_date = st.date_input("Starting date", value=date.today())
        selected = st.multiselect(
            "Choose materials",
            options=list(MATERIALS.keys()),
            default=["Fruit peels", "Dry leaves"],
            help="Select the materials you plan to combine.",
        )

        quantities = {}
        if selected:
            st.markdown("**Enter the quantity for each material**")
            for material in selected:
                quantities[material] = st.number_input(
                    f"{material} (kg)",
                    min_value=0.0,
                    value=1.0,
                    step=0.5,
                    key=f"planner_{material}",
                )
        else:
            st.write("Select at least one material to enter its quantity.")

        submitted = st.form_submit_button(
            "Calculate compost mixture",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        if not batch_name.strip():
            st.error("Please enter a batch name.")
        elif not selected:
            st.error("Please select at least one material.")
        elif not any(quantities.values()):
            st.error("Enter a quantity greater than zero for at least one material.")
        else:
            entries = [(material, quantities.get(material, 0.0)) for material in selected]
            result = make_recommendations(entries)
            green, brown, unsuitable, tips, cn_ratio, carbon_mass, nitrogen_mass, details, missing_data = result
            st.session_state.plan = {
                "name": batch_name.strip(),
                "start": start_date,
                "entries": entries,
                "green": green,
                "brown": brown,
                "unsuitable": unsuitable,
                "tips": tips,
                "cn_ratio": cn_ratio,
                "carbon_mass": carbon_mass,
                "nitrogen_mass": nitrogen_mass,
                "details": details,
                "missing_data": missing_data,
            }

    if "plan" not in st.session_state:
        return

    plan = st.session_state.plan
    st.markdown("---")
    st.markdown('<div class="section-title">Your mixture summary</div>', unsafe_allow_html=True)

    first, second, third = st.columns(3)
    first.metric("Green materials", f"{plan['green']:.1f} kg")
    second.metric("Brown materials", f"{plan['brown']:.1f} kg")
    third.metric("Unsuitable materials", len(plan["unsuitable"]))

    rows = [
        {"Material": material, "Category": MATERIALS[material][0], "Quantity (kg)": f"{quantity:.2f}"}
        for material, quantity in plan["entries"] if quantity > 0
    ]
    if rows:
        green_table(["Material", "Category", "Quantity (kg)"], [[r["Material"], r["Category"], r["Quantity (kg)"]] for r in rows])

    st.markdown('<div class="section-title">Estimated carbon-to-nitrogen ratio</div>', unsafe_allow_html=True)
    if plan["missing_data"]:
        st.warning(
            "The C:N ratio cannot be calculated for the complete mixture because a required "
            "reference value is unavailable for: " + ", ".join(plan["missing_data"]) + "."
        )
    elif plan["cn_ratio"] is None:
        st.warning("A C:N estimate is not available. Check that at least one suitable material has a positive quantity.")
    else:
        st.metric(
            "Estimated mixture C:N ratio",
            f"{plan['cn_ratio']:.1f}:1",
            help="Calculated from the wet-weight quantities and dry-basis carbon and nitrogen percentages, adjusted for each material's moisture content.",
        )

    if plan["details"]:
        st.markdown('<div class="section-title">Reference values and calculation details</div>', unsafe_allow_html=True)
        property_rows = []
        for item in plan["details"]:
            property_rows.append([
                item["material"],
                f"{item['quantity']:.2f}",
                f"{item['material_cn']:g}:1",
                f"{item['carbon_pct']:.2f}",
                f"{item['nitrogen_pct']:.2f}",
                f"{item['moisture_pct']:.1f}",
                item["source"],
            ])
        green_table(
            ["Material", "Wet weight (kg)", "C:N reference", "Carbon (%)", "Nitrogen (%)", "Moisture (%)", "Reference"],
            property_rows,
        )
        st.write(
            f"Estimated carbon contribution: {plan['carbon_mass']:.4f} kg. "
            f"Estimated nitrogen contribution: {plan['nitrogen_mass']:.4f} kg."
        )
        st.write(
            f"The general starting guideline is approximately {TARGET_CN_RATIO}:1. "
            "This is a guide rather than a pass-or-fail limit."
        )
    if plan["missing_data"]:
        st.warning("A complete C:N estimate is not available for: " + ", ".join(plan["missing_data"]) + ".")

    st.markdown('<div class="section-title">Suggestions</div>', unsafe_allow_html=True)
    for tip in plan["tips"]:
        st.write(tip)

    if st.button("Save this batch", type="primary"):
        st.session_state.batches.append({
            "name": plan["name"],
            "start_date": plan["start"],
            "materials": plan["entries"],
            "status": "Planning",
            "cn_ratio": plan["cn_ratio"],
        })
        st.success("Your batch has been saved. You can view it in Batch Tracking.")
