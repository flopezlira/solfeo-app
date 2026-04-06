"""Module 4: Interval reading quiz — embeds the HTML standalone app."""

import os
import streamlit.components.v1 as components


def render_intervals():
    html_path = os.path.join(os.path.dirname(__file__), "solfeo_intervalos.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=750, scrolling=False)
