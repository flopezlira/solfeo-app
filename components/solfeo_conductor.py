"""Module 2: Conducting pattern visualization — embeds the HTML standalone app."""

import os
import streamlit.components.v1 as components


def render_conductor():
    html_path = os.path.join(os.path.dirname(__file__), "solfeo_movimientos.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=850, scrolling=False)
