"""Compost guidance using a small set of predefined questions."""

import streamlit as st

from ui.components import page_heading


GUIDE_ANSWERS = {
    "Why does my compost smell bad?": (
        "A bad smell may mean the compost is too wet or does not have enough airflow. "
        "Add dry brown materials such as dry leaves or plain shredded cardboard, then mix gently."
    ),
    "What should I do if my compost is too wet?": (
        "Add dry brown materials such as dry leaves or plain shredded cardboard. Mix the pile "
        "gently and avoid adding more wet scraps until the moisture improves."
    ),
    "What should I do if my compost is too dry?": (
        "Add a little water and mix it evenly. Avoid soaking the pile. The mixture should feel "
        "similar to a wrung-out sponge."
    ),
    "Why is my compost decomposing slowly?": (
        "Slow decomposition can be related to moisture, airflow, material size or the mixture "
        "balance. Chop large scraps into smaller pieces, check the moisture and turn the mixture "
        "to improve airflow."
    ),
    "How can I prevent pests in my compost?": (
        "Cover fresh food scraps with brown materials, keep the compost area tidy and avoid "
        "adding meat or dairy to this beginner composting plan."
    ),
    "What are green materials?": (
        "Green materials are generally nitrogen-rich materials, such as fruit peels, vegetable "
        "scraps and fresh grass clippings. They provide nitrogen for microorganisms during decomposition."
    ),
    "What are brown materials?": (
        "Brown materials are generally carbon-rich materials, such as dry leaves, straw and plain "
        "cardboard. They provide carbon and help create air spaces in the compost mixture."
    ),
    "What does the C:N ratio mean?": (
        "The carbon-to-nitrogen (C:N) ratio compares the amount of carbon with the amount of "
        "nitrogen in a compost mixture. Cornell describes approximately 30:1 as a common starting "
        "guideline. The actual result depends on the materials used."
    ),
    "What is composting?": (
        "Composting is the natural process in which microorganisms break down organic materials "
        "into a more stable, soil-like product. A suitable balance of carbon, nitrogen, moisture "
        "and oxygen helps the process."
    ),
}


def render_guide():
    page_heading(
        "Compost Guide",
        "Compost Guide",
        "Choose a common composting question to view practical guidance."
    )

    st.markdown(
        '<div class="guide-banner">'
        '<div class="guide-banner-title">Composting help</div>'
        '<div class="guide-banner-copy">Select a question below to find a practical suggestion.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    question = st.selectbox(
        "Choose a question",
        options=list(GUIDE_ANSWERS.keys()),
        key="guide_question",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        show_answer = st.button("Show answer", type="primary", use_container_width=True)
    with col2:
        clear_answer = st.button("Clear answer", type="secondary", use_container_width=True)

    if clear_answer:
        st.session_state.pop("guide_answer", None)
        st.rerun()

    if show_answer:
        st.session_state.guide_answer = GUIDE_ANSWERS[question]

    if st.session_state.get("guide_answer"):
        st.markdown(
            '<div class="guide-answer">'
            '<div class="guide-answer-title">Suggestion</div>'
            f'<div>{st.session_state.guide_answer}</div>'
            '</div>',
            unsafe_allow_html=True,
        )
