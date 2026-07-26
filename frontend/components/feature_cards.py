import streamlit as st


def show_feature_cards():

    st.write("")
    st.write("")

    st.markdown(
        """
        <h2 style="text-align:center;color:#F4C430;">
        Why Choose FutureFund AI?
        </h2>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
### Portfolio Simulator

Simulate SIP, Lump Sum and Goal-based investments with realistic returns.
"""
        )

    with col2:
        st.info(
            """
### AI Advisor

Receive AI-powered investment suggestions based on your financial profile.
"""
        )

    col3, col4 = st.columns(2)

    with col3:
        st.info(
            """
### Goal Planner

Plan retirement, education, vacations or buying your dream home.
"""
        )

    with col4:
        st.info(
            """
### Market Insights

Visualize growth, inflation impact and portfolio performance.
"""
        )
        