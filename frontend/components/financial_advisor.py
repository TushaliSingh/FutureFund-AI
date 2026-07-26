import streamlit as st

from utils.recommendation_engine import generate_recommendation
from database.database import save_history


def show_financial_advisor():

    st.subheader("🤖 AI Financial Advisor")

    st.write(
        "Receive personalized investment guidance based on your financial profile."
    )

    # ----------------------------
    # Check Login
    # ----------------------------

    if "user" not in st.session_state:
        st.error("Please login first.")
        return

    user = st.session_state.user

    income = float(user[5])
    risk = str(user[6])
    expenses = float(user[7])
    savings = float(user[8])
    goal = str(user[9])
    experience = str(user[10])

    # ----------------------------
    # Session State
    # ----------------------------

    if "latest_recommendation" not in st.session_state:
        st.session_state.latest_recommendation = None

    # ----------------------------
    # Generate Recommendation
    # ----------------------------

    if st.button(
        "🚀 Generate Financial Advice",
        use_container_width=True
    ):

        recommendation = generate_recommendation(
            income=income,
            expenses=expenses,
            savings=savings,
            risk=risk,
            goal=goal,
            experience=experience
        )

        st.session_state.latest_recommendation = recommendation

        try:

            save_history(
                user_id=user[0],
                feature="AI Financial Advisor",
                result=f"Suggested SIP ₹{recommendation['sip']:,}"
            )

        except Exception as e:
            st.warning(f"History could not be saved.\n\n{e}")

    # ----------------------------
    # Display Recommendation
    # ----------------------------

    recommendation = st.session_state.latest_recommendation

    if recommendation is not None:

        st.divider()

        st.subheader("📈 Suggested Monthly SIP")

        st.metric(
            "Monthly SIP",
            f"₹{recommendation['sip']:,}"
        )

        st.divider()

        st.subheader("📊 Recommended Portfolio")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📈 Equity",
                f"{recommendation['portfolio']['Equity']}%"
            )

        with col2:
            st.metric(
                "🏦 Debt",
                f"{recommendation['portfolio']['Debt']}%"
            )

        with col3:
            st.metric(
                "🥇 Gold",
                f"{recommendation['portfolio']['Gold']}%"
            )

        st.progress(
            recommendation["portfolio"]["Equity"] / 100
        )

        st.divider()

        st.subheader("🎯 Investment Strategy")

        for strategy in recommendation["strategy"]:
            st.success(strategy)

        st.divider()

        st.subheader("💡 Improvement Suggestions")

        if recommendation["improvements"]:

            for item in recommendation["improvements"]:
                st.warning(item)

        else:

            st.success(
                "Excellent financial profile! Keep investing consistently."
            )

    else:

        st.info(
            "Click **Generate Financial Advice** to receive your personalized investment recommendations."
        )