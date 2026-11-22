"""The Home screen for Scrap2Soil."""

import streamlit as st
from data.materials import MATERIALS


def _navigate_to(target):
    """Update the sidebar navigation before Streamlit reruns the app."""
    st.session_state["navigation"] = target


def render_home():
    st.markdown(
        '<div class="welcome-line">Welcome to Scrap2Soil</div>'
        '<div class="welcome-copy">A little care for your scraps can help create healthier soil.</div>',
        unsafe_allow_html=True
    )

    hero_left, hero_right = st.columns([1.0, 1.0], vertical_alignment="center")
    with hero_left:
        st.markdown(
            '<div class="plant-dashboard">'
            '<div style="font-size:1.35rem;font-weight:900;color:#294B34;">Grow something good from waste.</div>'
            '<div style="color:#405443;line-height:1.5;margin-top:0.35rem;">'
            'Plan a balanced compost mixture, learn which materials to use and keep track of your batches.'
            '</div></div>',
            unsafe_allow_html=True
        )
        st.button(
            "＋  Plan a compost mixture",
            type="primary",
            use_container_width=True,
            on_click=_navigate_to,
            args=("Compost Planner",),
        )
    with hero_right:
        st.image("assets/compost_illustration.png", use_container_width=True)

    st.markdown('<div class="section-title">Explore Scrap2Soil</div>', unsafe_allow_html=True)
    feature_cols = st.columns(3)
    feature_data = [
        ("Compost Planner", "Build a mixture using the materials you have.", "Compost Planner"),
        ("Compost Guide", "Get simple tips for common compost issues.", "Compost Guide"),
        ("Batch Tracking", "Review your saved batches and their progress.", "Batch Tracking"),
    ]
    for col, (title, desc, target) in zip(feature_cols, feature_data):
        with col:
            st.markdown(
                f'<div class="plant-card">'
                f'<div class="plant-name">{title}</div>'
                f'<div class="plant-caption">{desc}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            st.button(
                "Open →",
                key=f"plant_home_{target}",
                use_container_width=True,
                on_click=_navigate_to,
                args=(target,),
            )

    st.markdown('<div class="section-title">Your compost overview</div>', unsafe_allow_html=True)
    total = len(st.session_state.batches)
    active = sum(b["status"] == "In Progress" for b in st.session_state.batches)
    completed = sum(b["status"] == "Completed" for b in st.session_state.batches)
    completion_pct = round((completed / total) * 100) if total else 0

    summary_cols = st.columns(3)
    summary = [
        (total, "Saved batches"),
        (active, "In progress"),
        (f"{completion_pct}%", "Completed batches"),
    ]
    for col, (value, label) in zip(summary_cols, summary):
        with col:
            st.markdown(
                f'<div class="stat-panel">'
                f'<div class="stat-number">{value}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True
            )

    if st.session_state.batches:
        recent = st.session_state.batches[-1]
        green_qty = sum(q for m, q in recent["materials"] if MATERIALS[m][0] == "Green")
        brown_qty = sum(q for m, q in recent["materials"] if MATERIALS[m][0] == "Brown")
        suitable_total = green_qty + brown_qty
        status_progress = {"Planning": 20, "In Progress": 65, "Completed": 100}
        stage_pct = status_progress.get(recent["status"], 0)

        st.markdown('<div class="section-title">Latest compost batch</div>', unsafe_allow_html=True)
        batch_left, batch_right = st.columns([1.1, 0.9])
        with batch_left:
            with st.container(border=True):
                st.markdown(f"**{recent['name']}**")
                st.write(f"Started {recent['start_date']} · {recent['status']}")
                st.markdown(
                    f'<div class="batch-progress-label"><span>Stage indicator</span><span>{stage_pct}%</span></div>',
                    unsafe_allow_html=True
                )
                st.progress(stage_pct / 100)
                st.markdown(
                    '<div class="percentage-note">This is a visual stage indicator based on the status you selected, not a sensor measurement of decomposition.</div>',
                    unsafe_allow_html=True
                )
        with batch_right:
            with st.container(border=True):
                st.markdown("**Green and brown material mix**")
                if suitable_total > 0:
                    green_pct = round(green_qty / suitable_total * 100)
                    brown_pct = 100 - green_pct
                    st.markdown(
                        f'<div class="mix-track"><div class="mix-green" style="width:{green_pct}%"></div>'
                        f'<div class="mix-brown" style="width:{brown_pct}%"></div></div>'
                        f'<div class="mix-legend"><span>Green {green_pct}%</span>'
                        f'<span>Brown {brown_pct}%</span></div>',
                        unsafe_allow_html=True
                    )
                    st.write(f"Based on {suitable_total:g} kg of suitable materials in this batch.")
                else:
                    st.info("Add suitable green or brown materials to view the mix percentages.")
    else:
        st.markdown(
            '<div class="plant-dashboard"><b style="color:#294B34;">Your first batch will appear here.</b><br>'
            '<span style="color:#405443;">Create a compost plan to see your batch progress and green/brown material percentages.</span></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="green-note">Percentages are calculated from quantities and batch statuses entered in the prototype. '
        'No live moisture, humidity or decomposition sensors are connected.</div>',
        unsafe_allow_html=True
    )

