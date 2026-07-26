import streamlit as st

from utils.api_client import calculate_sip
from components.lumpsum_simulator import show_lumpsum_simulator
from components.goal_planner import show_goal_planner
from components.inflation_calculator import show_inflation_calculator
from components.cagr_calculator import show_cagr_calculator


def show_sip_simulator():

    st.subheader("📈 SIP Calculator")

    monthly_sip = st.number_input(
        "Monthly SIP (₹)",
        min_value=500,
        value=5000,
        step=500,
        key="sip_amount"
    )

    expected_return = st.number_input(
        "Expected Annual Return (%)",
        min_value=0.0,
        max_value=30.0,
        value=12.0,
        step=0.5,
        key="sip_return"
    )

    years = st.number_input(
        "Investment Duration (Years)",
        min_value=1,
        max_value=50,
        value=20,
        key="sip_years"
    )

    if st.button(
        "Calculate SIP",
        use_container_width=True
    ):

        try:

            result = calculate_sip(
                monthly_investment=monthly_sip,
                annual_return=expected_return,
                years=years,
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
                    "💰 Maturity Value",
                    f"₹{result['maturity_value']:,.2f}"
                )

        except Exception as e:
            st.error(f"Backend connection failed: {e}")


def show_investment_simulator():

    st.header("📈 Investment Simulator")

    sip_tab, lump_tab, goal_tab, inflation_tab, cagr_tab = st.tabs(
        [
            "📈 SIP",
            "💰 Lump Sum",
            "🎯 Goal Planner",
            "💸 Inflation",
            "📊 CAGR"
        ]
    )

    with sip_tab:
        show_sip_simulator()

    with lump_tab:
        show_lumpsum_simulator()

    with goal_tab:
        show_goal_planner()

    with inflation_tab:
        show_inflation_calculator()

    with cagr_tab:
        show_cagr_calculator()