import streamlit as st
from utils.investment_engine import lumpsum_calculator


def show_lumpsum_simulator():

    st.subheader("💰 Lump Sum Investment Calculator")

    principal = st.number_input(
        "Investment Amount (₹)",
        min_value=1000,
        value=100000,
        step=1000,
        key="lump_principal"
    )

    annual_return = st.number_input(
        "Expected Annual Return (%)",
        min_value=0.0,
        max_value=30.0,
        value=12.0,
        step=0.5,
        key="lump_return"
    )

    years = st.number_input(
        "Investment Duration (Years)",
        min_value=1,
        max_value=50,
        value=20,
        key="lump_years"
    )

    if st.button("Calculate Lump Sum", use_container_width=True):

        result = lumpsum_calculator(
            principal=principal,
            annual_return=annual_return,
            years=years
        )

        st.subheader("📊 Investment Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💵 Invested Amount",
                f"₹{result['invested_amount']:,.2f}"
            )

        with col2:
            st.metric(
                "📈 Estimated Returns",
                f"₹{result['estimated_returns']:,.2f}"
            )

        with col3:
            st.metric(
                "💰 Future Value",
                f"₹{result['maturity_value']:,.2f}"
            )