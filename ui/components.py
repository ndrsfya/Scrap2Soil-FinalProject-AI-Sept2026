"""Reusable UI components."""

import streamlit as st

def page_heading(kicker, title, description):
    st.markdown(f'<div class="page-kicker">{kicker}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-desc">{description}</div>', unsafe_allow_html=True)
