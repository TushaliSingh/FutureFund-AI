import streamlit as st
from utils.investment_engine import cagr_calculator


def show_cagr_calculator():

    st.subheader("📊 CAGR Calculator")

    initial_value = st.number_input(
        "Initial Investment (₹)",
        min_value=1000,
        value=100000,
        step=1000,
        key="cagr_initial"
    )

    final_value = st.number_input(
        "Final Value (₹)",
        min_value=1000,
        value=300000,
        step=1000,
        key="cagr_final"
    )

    years = st.number_input(
        "Investment Duration (Years)",
        min_value=1,
        max_value=50,
        value=10,
        key="cagr_years"
    )

    if st.button(
        "Calculate CAGR",
        use_container_width=True
    ):

        result = cagr_calculator(
            initial_value=initial_value,
            final_value=final_value,
            years=years
        )

        st.subheader("📈 CAGR Result")

        st.metric(
            "Annual CAGR",
            f"{result['cagr']:.2f}%"
        )

        st.success(
            f"Your investment grew at an average annual rate of {result['cagr']:.2f}%."
        )