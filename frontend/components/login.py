import streamlit as st

from database.database import get_user
from utils.auth import verify_password


def show_login():

    st.title("🔑 Login")
    st.write("Welcome back!")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        user = get_user(email)

        if user is None:
            st.error("User not found.")
            return

        stored_password = user[3]

        if verify_password(password, stored_password):

            st.session_state.logged_in = True
            st.session_state.user = user
            st.session_state.page = "dashboard"

            st.rerun()

        else:
            st.error("Incorrect password.")

    st.divider()

    if st.button(
        "Create New Account",
        use_container_width=True
    ):
        st.session_state.page = "signup"
        st.rerun()