"""Reusable interface components."""

from html import escape

import streamlit as st


def page_heading(kicker, title, description):
    st.markdown(f'<div class="page-title">{escape(title)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-desc">{escape(description)}</div>', unsafe_allow_html=True)


def green_table(headers, rows):
    """Display a readable table using the application's green colour theme."""
    header_html = "".join(f"<th>{escape(str(header))}</th>" for header in headers)
    row_html = []
    for row in rows:
        cells = "".join(f"<td>{escape(str(value))}</td>" for value in row)
        row_html.append(f"<tr>{cells}</tr>")

    st.markdown(
        '<div class="green-table-wrap"><table class="green-table">'
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{''.join(row_html)}</tbody>"
        '</table></div>',
        unsafe_allow_html=True,
    )
