"""Solfeo — Entrenador de lectura musical (Streamlit)."""

import html as _html
import pathlib
import subprocess

import streamlit as st

_REPO_ROOT = pathlib.Path(__file__).resolve().parent


def _get_last_update() -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=format:%d/%m/%Y %H:%M"],
            capture_output=True, text=True, timeout=2,
            cwd=_REPO_ROOT,
        )
        raw = result.stdout.strip()
        return _html.escape(raw) if raw else "—"
    except Exception:
        return "—"


st.set_page_config(
    page_title="Solfeo",
    page_icon="🎵",
    layout="centered",
)

st.markdown(
    "<h1 style='text-align:center; color:#7a7468; letter-spacing:0.1em;'>"
    "SOLFEO</h1>"
    "<p style='text-align:center; color:#9a9282; font-size:0.9em;'>"
    "Entrenador de lectura musical</p>"
    "<p style='text-align:center; color:#b0a898; font-size:0.72em;'>"
    "por Francisco López-Lira · flopezlira@gmail.com</p>"
    f"<p style='text-align:center; color:#c8c0b4; font-size:0.6em;'>"
    f"Última actualización: {_get_last_update()}</p>",
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.tabs(["🎵 Notas", "🎼 Dirección", "🎶 Notas + Dirección", "🎵 Intervalos"])

with tab1:
    from components.solfeo_quiz import render_quiz
    render_quiz()

with tab2:
    from components.solfeo_conductor import render_conductor
    render_conductor()

with tab3:
    from components.solfeo_combined import render_combined
    render_combined()

with tab4:
    from components.solfeo_intervals import render_intervals
    render_intervals()
