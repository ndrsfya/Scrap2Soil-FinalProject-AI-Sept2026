"""The Batch Tracking screen for Scrap2Soil."""

import streamlit as st
from datetime import timedelta
from data.materials import MATERIALS
from ui.components import page_heading


def render_tracking():
    page_heading(
        "KEEP AN EYE ON PROGRESS",
        "Batch Tracking",
        "View saved compost batches, update their status and check suggested reminders."
    )

    if not st.session_state.batches:
        st.info("You have not saved any batches yet. Create one in Compost Planner first.")
    else:
        st.markdown(
            '<div class="plant-dashboard"><b style="color:#294B34;">Your compost batches</b><br>'
            '<span style="color:#405443;">Update a batch status to change its stage indicator. Percentages are illustrative and are not measured by sensors.</span></div>',
            unsafe_allow_html=True
        )
        progress_values = {"Planning": 20, "In Progress": 65, "Completed": 100}
        for i, batch in enumerate(st.session_state.batches):
            with st.container(border=True):
                top_left, top_right = st.columns([3, 1])
                with top_left:
                    st.markdown(f"**{batch['name']}**")
                    st.caption(f"Started on {batch['start_date']}")
                with top_right:
                    st.markdown(f"**{batch['status']}**")

                stage_pct = progress_values[batch["status"]]
                st.markdown(
                    f'<div class="batch-progress-label"><span>Stage indicator</span><span>{stage_pct}%</span></div>',
                    unsafe_allow_html=True
                )
                st.progress(stage_pct / 100)
                st.markdown(
                    '<div class="percentage-note">Illustrative progress based on the selected status, not actual compost maturity.</div>',
                    unsafe_allow_html=True
                )

                green_qty = sum(q for m, q in batch["materials"] if MATERIALS[m][0] == "Green")
                brown_qty = sum(q for m, q in batch["materials"] if MATERIALS[m][0] == "Brown")
                suitable_total = green_qty + brown_qty
                if suitable_total > 0:
                    green_pct = round(green_qty / suitable_total * 100)
                    brown_pct = 100 - green_pct
                    st.markdown("**Material composition**")
                    st.markdown(
                        f'<div class="mix-track"><div class="mix-green" style="width:{green_pct}%"></div>'
                        f'<div class="mix-brown" style="width:{brown_pct}%"></div></div>'
                        f'<div class="mix-legend"><span>Green: {green_pct}%</span>'
                        f'<span>Brown: {brown_pct}%</span></div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.caption("No suitable green/brown material quantities are available for a composition percentage.")

                st.write("**Materials:** " + ", ".join(f"{m} ({q:g} kg)" for m, q in batch["materials"]))
                reminder1 = batch["start_date"] + timedelta(days=3)
                reminder2 = batch["start_date"] + timedelta(days=7)
                r1, r2 = st.columns(2)
                r1.caption(f"Moisture check: {reminder1}")
                r2.caption(f"Turning check: {reminder2}")

                options = ["Planning", "In Progress", "Completed"]
                current_index = options.index(batch["status"])
                new_status = st.selectbox(
                    "Update progress",
                    options,
                    index=current_index,
                    key=f"batch_status_{i}"
                )
                if st.button("Save status", key=f"update_batch_{i}"):
                    st.session_state.batches[i]["status"] = new_status
                    st.success("Batch status updated.")
                    st.rerun()

    # -----------------------------
    # About
    # -----------------------------
