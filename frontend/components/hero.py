import streamlit as st


def show_hero():

    st.markdown(
        """
        <h1 style='text-align:center;
        color:#F4C430;
        font-size:70px;'>
        FutureFund AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align:center;
        font-size:28px;
        color:white;'>
        Your Personal AI Investment Simulator
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align:center;
        color:#BBBBBB;
        font-size:20px;
        width:70%;
        margin:auto;'>
        Invest smarter with AI-powered portfolio recommendations,
        realistic investment simulations and long-term financial planning.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    c1, c2, c3 = st.columns([2, 2, 2])

    with c2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.write("")