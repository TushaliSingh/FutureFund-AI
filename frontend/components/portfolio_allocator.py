import streamlit as st

from utils.investment_engine import portfolio_allocation


def show_portfolio_allocator():

    st.subheader("🥧 Portfolio Allocation Advisor")

    st.write(
        "Get a suggested investment allocation based on your age and risk appetite."
    )

    if "user" not in st.session_state:
        st.error("Please login first.")
        return

    user = st.session_state.user

    age = int(user[4])
    risk = str(user[6])

    st.info(
        f"Based on your profile:\n\nAge: {age}\n\nRisk Appetite: {risk}"
    )

    if st.button(
        "Generate Portfolio",
        use_container_width=True
    ):

        allocation = portfolio_allocation(
            age=age,
            risk_level=risk
        )

        st.subheader("📊 Recommended Allocation")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📈 Equity",
                f"{allocation['Equity']}%"
            )

        with col2:
            st.metric(
                "🏦 Debt",
                f"{allocation['Debt']}%"
            )

        with col3:
            st.metric(
                "🥇 Gold",
                f"{allocation['Gold']}%"
            )

        st.progress(allocation["Equity"] / 100)

        st.success(
            "Portfolio generated successfully based on your age and risk profile."
        )

        st.write("### 📌 Investment Advice")

        if risk.lower() == "low":
            st.info(
                "You prefer stability. Most of your investments are allocated to Debt with moderate Equity exposure."
            )

        elif risk.lower() == "medium":
            st.info(
                "A balanced portfolio with healthy Equity exposure for long-term wealth creation."
            )

        else:
            st.info(
                "You have a high risk appetite. Your portfolio is Equity-heavy to maximize long-term growth."
            )