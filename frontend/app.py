from components.signup import show_signup
from components.login import show_login
from components.dashboard import show_dashboard

import streamlit as st
from pathlib import Path

from components.hero import show_hero
from components.feature_cards import show_feature_cards
from components.how_it_works import show_how_it_works

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="FutureFund AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- Session ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- CSS ----------------

css_file = Path(__file__).parent / "styles" / "style.css"

if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# NAVBAR
# ==========================================================

if st.session_state.get("logged_in", False):

    c1, c2, c3 = st.columns([8, 2, 2])

    with c1:
        st.markdown("## 💰 FutureFund AI")

    with c2:
        if st.button("Dashboard"):
            st.session_state.page = "dashboard"

    with c3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.pop("user", None)
            st.session_state.page = "home"
            st.rerun()

else:

    c1, c2 = st.columns([10, 2])

    with c1:
        st.markdown("## 💰 FutureFund AI")

    with c2:
        if st.button("Home"):
            st.session_state.page = "home"

st.divider()

# ==========================================================
# ROUTING
# ==========================================================

if st.session_state.page == "home":

    show_hero()
    show_feature_cards()
    show_how_it_works()

elif st.session_state.page == "login":

    show_login()

elif st.session_state.page == "signup":

    show_signup()

elif st.session_state.page == "dashboard":

    show_dashboard()