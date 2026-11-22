"""Project information screen."""

import streamlit as st

from data.materials import MATERIALS, COMPOST_PROPERTIES, TARGET_CN_RATIO
from ui.components import page_heading, green_table


def render_about():
    page_heading(
        "ABOUT THIS PROJECT",
        "About Scrap2Soil",
        "A student project exploring how a digital tool can support better organic waste management."
    )

    st.markdown(
        '<div class="green-note">Scrap2Soil helps UTP students, staff and cafeteria operators plan compost mixtures, '
        'learn about suitable materials and keep track of compost batches.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">What this prototype can do</div>', unsafe_allow_html=True)
    st.write("Classify selected materials as green, brown or unsuitable.")
    st.write("Estimate a compost mixture's carbon-to-nitrogen (C:N) ratio using material reference values.")
    st.write(f"Provide suggestions using an approximate starting target of {TARGET_CN_RATIO}:1.")
    st.write("Give guidance for common composting problems and track batches during the current app session.")

    st.markdown('<div class="section-title">Material guide</div>', unsafe_allow_html=True)
    material_rows = []
    for name, details in MATERIALS.items():
        properties = COMPOST_PROPERTIES.get(name)
        row = {"Material": name, "Category": details[0], "Guidance": details[1]}
        if properties:
            row["Reference C:N"] = f"{properties['cn_ratio']:g}:1"
            row["Reference moisture"] = (
                f"{properties['moisture']:g}%" if properties["moisture"] is not None else "Not available"
            )
        else:
            row["Reference C:N"] = "Not available"
            row["Reference moisture"] = "Not available"
        material_rows.append(row)
    material_headers = ["Material", "Category", "Guidance", "Reference C:N", "Reference moisture"]
    green_table(material_headers, [[row.get(header, "Not available") for header in material_headers] for row in material_rows])

    st.markdown('<div class="section-title">How the C:N estimate works</div>', unsafe_allow_html=True)
    st.write(
        "The planner follows Cornell's wet-weight mixture method. It uses each material's wet weight, "
        "carbon percentage, nitrogen percentage and moisture content to estimate the total carbon and "
        "nitrogen contributions. The total carbon is divided by the total nitrogen to obtain the mixture "
        "C:N ratio. Carbon percentage is derived from nitrogen percentage multiplied by the material's C:N ratio."
    )

    st.markdown('<div class="section-title">Reference</div>', unsafe_allow_html=True)
    st.markdown(
        "[Cornell University: C/N Ratio and Mixture Calculation](https://compost.css.cornell.edu/calc/cn_ratio.html)  \n"
        "[Cornell Waste Management Institute: On-Farm Composting Handbook, Appendix A](https://cwmi.css.cornell.edu/AppendixATable1OFCH.pdf)"
    )

    st.markdown('<div class="section-title">System limitations</div>', unsafe_allow_html=True)
    st.write(
        "The C:N result is an estimate based on typical published material values, not a laboratory measurement "
        "of the user's actual waste. Some materials do not have complete reference data and cannot be included "
        "in a calculated mixture until suitable values are available. Users enter quantities manually; no sensors "
        "or trained machine-learning model are connected, and batch records remain in the current app session."
    )
