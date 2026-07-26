import streamlit as st
from utils.investment_engine import inflation_calculator


def show_inflation_calculator():

    st.subheader("💸 Inflation Calculator")

    current_amount = st.number_input(
        "Current Amount (₹)",
        min_value=1000,
        value=100000,
        step=1000,
        key="inflation_amount"
    )

    inflation_rate = st.number_input(
        "Inflation Rate (%)",
        min_value=0.0,
        max_value=20.0,
        value=6.0,
        step=0.5,
        key="inflation_rate"
    )

    years = st.number_input(
        "Years",
        min_value=1,
        max_value=50,
        value=20,
        key="inflation_years"
    )

    if st.button(
        "Calculate Inflation",
        use_container_width=True
    ):

        result = inflation_calculator(
            current_amount=current_amount,
            inflation_rate=inflation_rate,
            years=years
        )

        st.subheader("📊 Result")

        st.metric(
            "Future Cost",
            f"₹{result['future_value']:,.2f}"
        )