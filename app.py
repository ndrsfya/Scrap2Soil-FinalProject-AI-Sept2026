"""Scrap2Soil Streamlit application entry point."""

import streamlit as st

from ui.styles import apply_styles
from app_pages.home import render_home
from app_pages.planner import render_planner
from app_pages.guide import render_guide
from app_pages.tracking import render_tracking
from app_pages.about import render_about


def main():
    st.set_page_config(
        page_title="Scrap2Soil | Compost Planner",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    apply_styles(st)

    if "navigation" not in st.session_state:
        st.session_state.navigation = "Home"
    if "batches" not in st.session_state:
        st.session_state.batches = []
    with st.sidebar:
        st.markdown('<div class="brand">Scrap2Soil</div>', unsafe_allow_html=True)
        st.markdown('<div class="brand-sub">A simpler way to plan compost</div>', unsafe_allow_html=True)
        page = st.radio(
            "MENU",
            ["Home", "Compost Planner", "Compost Guide", "Batch Tracking", "About"],
            label_visibility="visible",
            key="navigation"
        )

    if page == "Home":
        render_home()
    elif page == "Compost Planner":
        render_planner()
    elif page == "Compost Guide":
        render_guide()
    elif page == "Batch Tracking":
        render_tracking()
    else:
        render_about()



if __name__ == "__main__":
    main()
