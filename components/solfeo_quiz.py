"""Module 1: Note identification quiz — embeds the HTML standalone app."""

import os
import streamlit.components.v1 as components


def render_quiz():
    html_path = os.path.join(os.path.dirname(__file__), "solfeo_clave_sol.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=850, scrolling=False)
