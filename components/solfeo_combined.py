"""Module 3: Beat-synchronized note quiz — embeds the HTML standalone app."""

import os
import streamlit.components.v1 as components


def render_combined():
    html_path = os.path.join(os.path.dirname(__file__), "solfeo_unificado.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=750, scrolling=False)
