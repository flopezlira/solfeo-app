"""Solfeo — Entrenador de lectura musical (Streamlit)."""

import streamlit as st

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
    "por Francisco López-Lira · flopezlira@gmail.com</p>",
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs(["🎵 Identificación de Notas", "🎼 Movimientos de Dirección", "🎶 Notas + Dirección"])

with tab1:
    from components.solfeo_quiz import render_quiz
    render_quiz()

with tab2:
    from components.solfeo_conductor import render_conductor
    render_conductor()

with tab3:
    from components.solfeo_combined import render_combined
    render_combined()
