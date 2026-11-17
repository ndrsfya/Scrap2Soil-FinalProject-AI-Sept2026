"""The Compost Guide screen for Scrap2Soil."""

import streamlit as st
from logic.compost_logic import chat_answer
from ui.components import page_heading


def render_guide():
    page_heading(
        "GROW WITH CONFIDENCE",
        "Compost Guide",
        "Simple tips to help you build a healthy compost mixture and solve common problems."
    )

    st.markdown(
        '<div class="guide-banner">'
        '<div class="guide-banner-icon">🌱</div>'
        '<div><div class="guide-banner-title">A little help for your compost journey</div>'
        '<div class="guide-banner-copy">Choose a common issue below to get a practical suggestion. '
        'You can also ask the Scrap2Soil assistant a question.</div></div></div>',
        unsafe_allow_html=True
    )

    common_questions = {
        "My compost smells bad": "A bad smell may mean the pile is too wet or lacks airflow. Add dry brown materials such as leaves or shredded cardboard, then mix gently to improve airflow.",
        "My compost is too wet": "Add dry brown materials such as dry leaves or shredded cardboard. Mix gently and avoid adding more wet scraps until the mixture is better balanced.",
        "My compost is too dry": "Add a little water and mix evenly. Avoid soaking the pile. The moisture should feel similar to a wrung-out sponge.",
        "Decomposition is slow": "Check moisture, airflow and material size. Chop scraps into smaller pieces, mix gently and review the green/brown balance.",
        "There are pests around my compost": "Cover fresh food scraps with brown material, avoid meat and dairy in this beginner plan, and keep the compost area tidy."
    }

    st.markdown('<div class="guide-section-heading">🌿 What do you need help with?</div>', unsafe_allow_html=True)
    issue_cols = st.columns(5)
    issue_data = [
        ("💧", "Too wet", "Add dry brown materials"),
        ("☀️", "Too dry", "Check moisture"),
        ("🍃", "Bad smell", "Improve airflow"),
        ("🐌", "Slow compost", "Check the mixture"),
        ("🐛", "Pests", "Cover food scraps"),
    ]
    for col, (icon, title, desc) in zip(issue_cols, issue_data):
        with col:
            st.markdown(
                f'<div class="guide-issue"><div class="guide-issue-icon">{icon}</div>'
                f'<div class="guide-issue-title">{title}</div>'
                f'<div class="guide-issue-copy">{desc}</div></div>',
                unsafe_allow_html=True
            )

    with st.container(border=True):
        st.markdown('<div class="guide-section-heading">Select a common composting issue</div>', unsafe_allow_html=True)
        choice = st.selectbox(
            "Choose the issue you are experiencing",
            list(common_questions.keys()),
            key="guide_issue_select"
        )
        if st.button("Show suggestion", type="primary", key="show_guide_suggestion"):
            st.session_state.guide_answer = common_questions[choice]
        if "guide_answer" in st.session_state:
            st.markdown(
                '<div class="guide-answer">🌿 ' + st.session_state.guide_answer + '</div>',
                unsafe_allow_html=True
            )

    st.markdown('<div class="guide-section-heading">💬 Need a quick answer?</div>', unsafe_allow_html=True)
    quick_cols = st.columns(3)
    quick_prompts = [
        ("🍃", "Why does it smell bad?"),
        ("💧", "What if it is too wet?"),
        ("🌱", "How do I balance green and brown?")
    ]
    for quick_col, (icon, quick_prompt) in zip(quick_cols, quick_prompts):
        with quick_col:
            if st.button(f"{icon}  {quick_prompt}", key="quick_" + quick_prompt, use_container_width=True):
                st.session_state.chat.append(("user", quick_prompt))
                st.session_state.chat.append(("assistant", chat_answer(quick_prompt)))
                st.rerun()

    st.markdown('<div class="guide-section-heading">🌼 Ask the Scrap2Soil assistant</div>', unsafe_allow_html=True)
    for role, message in st.session_state.chat:
        with st.chat_message(role):
            st.write(message)
    prompt = st.chat_input("Type your composting question here...")
    if prompt:
        st.session_state.chat.append(("user", prompt))
        st.session_state.chat.append(("assistant", chat_answer(prompt)))
        st.rerun()

    if st.button("Clear conversation"):
        st.session_state.chat = [
            ("assistant", "Hello! Tell me what is happening with your compost and I will suggest a few basic steps.")
        ]
        st.rerun()

    # -----------------------------
    # Batch Tracking
    # -----------------------------
