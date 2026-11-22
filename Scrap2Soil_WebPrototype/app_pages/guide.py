"""Compost guidance page."""

import streamlit as st
from ui.components import page_heading


def render_guide():
    page_heading(
        "COMPOSTING TIPS",
        "Compost Guide",
        "Simple advice for common composting problems."
    )

    st.markdown(
        '<div class="guide-banner">'
        '<div><div class="guide-banner-title">Help for your compost</div>'
        '<div class="guide-banner-copy">Choose an issue to view practical steps you can try.</div></div></div>',
        unsafe_allow_html=True
    )

    common_questions = {
        "My compost smells bad": "A bad smell may mean the pile is too wet or lacks airflow. Add dry brown materials such as leaves or shredded cardboard, then mix gently to improve airflow.",
        "My compost is too wet": "Add dry brown materials such as dry leaves or shredded cardboard. Mix gently and avoid adding more wet scraps until the mixture is better balanced.",
        "My compost is too dry": "Add a little water and mix evenly. Avoid soaking the pile. The moisture should feel similar to a wrung-out sponge.",
        "Decomposition is slow": "Check moisture, airflow and material size. Chop scraps into smaller pieces, mix gently and review the green/brown balance.",
        "There are pests around my compost": "Cover fresh food scraps with brown material, avoid meat and dairy in this beginner plan, and keep the compost area tidy."
    }

    with st.container(border=True):
        st.markdown(
            '<div class="guide-section-heading">Select a common composting issue</div>',
            unsafe_allow_html=True
        )
        choice = st.selectbox(
            "Choose the issue you are experiencing",
            list(common_questions.keys()),
            key="guide_issue_select"
        )
        if st.button("Show suggestion", type="primary", key="show_guide_suggestion"):
            st.session_state.guide_answer = common_questions[choice]

        if "guide_answer" in st.session_state:
            st.markdown(
                '<div class="guide-answer">' + st.session_state.guide_answer + '</div>',
                unsafe_allow_html=True
            )
