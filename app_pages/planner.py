"""The Compost Planner screen for Scrap2Soil."""

import streamlit as st
from datetime import date
from data.materials import MATERIALS
from logic.compost_logic import make_recommendations
from ui.components import page_heading


def render_planner():
    page_heading(
        "PLAN YOUR MIXTURE",
        "Compost Planner",
        "Add the materials you have and enter an estimated quantity in kilograms."
    )

    st.markdown(
        '<div class="green-note">A simple starting point is to combine green materials (such as fruit and vegetable scraps) with brown materials (such as dry leaves and cardboard).</div>',
        unsafe_allow_html=True
    )

    with st.form("planner_form"):
        batch_name = st.text_input("Batch name", placeholder="e.g. Cafeteria food waste")
        start_date = st.date_input("Starting date", value=date.today())
        selected = st.multiselect(
            "Choose materials",
            options=list(MATERIALS.keys()),
            default=["Fruit peels", "Dry leaves"],
            help="You can select more than one material."
        )

        quantities = {}
        if selected:
            st.markdown("**Enter quantity for each selected material**")
            for material in selected:
                quantities[material] = st.number_input(
                    f"{material} (kg)",
                    min_value=0.0,
                    value=1.0,
                    step=0.5,
                    key=f"planner_{material}"
                )
        else:
            st.caption("Select at least one material to enter its quantity.")

        submitted = st.form_submit_button("Get compost suggestions", type="primary", use_container_width=True)

    if submitted:
        if not batch_name.strip():
            st.error("Please enter a batch name.")
        elif not selected:
            st.error("Please select at least one material.")
        else:
            entries = [(m, quantities.get(m, 0.0)) for m in selected]
            green, brown, unsuitable, tips = make_recommendations(entries)
            st.session_state.plan = {
                "name": batch_name.strip(),
                "start": start_date,
                "entries": entries,
                "green": green,
                "brown": brown,
                "unsuitable": unsuitable,
                "tips": tips
            }

    if "plan" in st.session_state:
        plan = st.session_state.plan
        st.markdown("---")
        st.markdown('<div class="section-title">Your mixture summary</div>', unsafe_allow_html=True)

        a, b, c = st.columns(3)
        a.metric("Green materials", f"{plan['green']:.1f} kg")
        b.metric("Brown materials", f"{plan['brown']:.1f} kg")
        c.metric("Unsuitable materials", len(plan["unsuitable"]))

        rows = []
        for material, qty in plan["entries"]:
            if qty > 0:
                category = MATERIALS[material][0]
                rows.append({"Material": material, "Category": category, "Quantity (kg)": f"{qty:.1f}"})
        if rows:
            st.table(rows)

        total = plan["green"] + plan["brown"]
        if total > 0:
            st.markdown("**Green and brown material balance**")
            st.progress(plan["green"] / total)
            st.caption(f"Green: {plan['green']:.1f} kg · Brown: {plan['brown']:.1f} kg")

        st.markdown('<div class="section-title">Suggestions</div>', unsafe_allow_html=True)
        for tip in plan["tips"]:
            st.write("• " + tip)

        if st.button("Save this batch", type="primary"):
            st.session_state.batches.append({
                "name": plan["name"],
                "start_date": plan["start"],
                "materials": plan["entries"],
                "status": "Planning"
            })
            st.success("Your batch has been saved. You can view it in Batch Tracking.")

    # -----------------------------
    # Compost Guide / assistant
    # -----------------------------
