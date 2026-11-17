"""The About screen for Scrap2Soil."""

import streamlit as st
from data.materials import MATERIALS
from ui.components import page_heading


def render_about():
    page_heading(
        "ABOUT THIS PROJECT",
        "About Scrap2Soil",
        "A student project exploring how a digital assistant can support better organic waste management."
    )

    st.markdown(
        '<div class="green-note">Scrap2Soil is designed to help UTP students, staff and cafeteria operators plan compost mixtures, learn about suitable materials and keep track of compost batches.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">What this prototype can do</div>', unsafe_allow_html=True)
    st.write("• Classify selected materials as green, brown or unsuitable.")
    st.write("• Estimate the quantity of green and brown materials.")
    st.write("• Provide basic suggestions for improving a mixture.")
    st.write("• Give keyword-based guidance for common composting problems.")
    st.write("• Save batches during the current app session and update their status.")

    st.markdown('<div class="section-title">Material guide</div>', unsafe_allow_html=True)
    material_rows = [
        {"Material": name, "Category": details[0], "Guidance": details[1]}
        for name, details in MATERIALS.items()
    ]
    st.table(material_rows)

    st.markdown('<div class="section-title">Current prototype limitations</div>', unsafe_allow_html=True)
    st.write("• Recommendations use predefined material information and simple rules.")
    st.write("• The guide responds using keyword matching; it is not a trained machine-learning model.")
    st.write("• Users enter quantities manually. No temperature, moisture or pH sensors are connected.")
    st.write("• Batch records are stored in the current app session. A database would be needed for permanent, multi-user storage.")
