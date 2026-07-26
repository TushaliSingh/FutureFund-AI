import streamlit as st

from utils.investment_engine import goal_sip_calculator


def show_goal_planner():

    st.subheader("🎯 Goal-Based Investment Planner")

    target_amount = st.number_input(
        "Target Amount (₹)",
        min_value=100000,
        value=5000000,
        step=100000,
        key="goal_target"
    )

    annual_return = st.number_input(
        "Expected Annual Return (%)",
        min_value=0.0,
        max_value=30.0,
        value=12.0,
        step=0.5,
        key="goal_return"
    )

    years = st.number_input(
        "Years to Achieve Goal",
        min_value=1,
        max_value=50,
        value=15,
        key="goal_years"
    )

    if st.button(
        "Calculate Required SIP",
        use_container_width=True
    ):

        result = goal_sip_calculator(
            target_amount=target_amount,
            annual_return=annual_return,
            years=years
        )

        st.subheader("📊 Goal Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💸 Required Monthly SIP",
                f"₹{result['required_monthly_sip']:,.2f}"
            )

        with col2:
            st.metric(
                "💵 Total Investment",
                f"₹{result['invested_amount']:,.2f}"
            )

        with col3:
            st.metric(
                "🎯 Target Amount",
                f"₹{result['target_amount']:,.2f}"
            )

        st.success(
            f"If you invest approximately ₹{result['required_monthly_sip']:,.0f} every month for {years} years at an expected annual return of {annual_return}%, you can work toward your target of ₹{result['target_amount']:,.0f}."
        )