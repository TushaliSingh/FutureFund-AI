import streamlit as st
from pathlib import Path

from components.hero import show_hero
from components.feature_cards import show_feature_cards
from components.how_it_works import show_how_it_works

css_file = Path(__file__).parent.parent / "styles" / "style.css"

if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text()}</style>",
        unsafe_allow_html=True,
    )

show_hero()
show_feature_cards()
show_how_it_works()