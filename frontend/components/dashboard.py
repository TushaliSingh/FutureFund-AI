import streamlit as st

from components.analytics_dashboard import show_analytics_dashboard
from components.financial_charts import show_financial_charts
from components.investment_simulator import show_investment_simulator
from components.portfolio_allocator import show_portfolio_allocator
from components.financial_advisor import show_financial_advisor

from utils.financial_score import calculate_financial_score
from utils.pdf_report import generate_financial_report
from utils.export_history import (
    history_to_csv,
    history_to_excel
)

from database.database import get_history


def show_dashboard():

    # ---------------- Authentication ----------------

    if not st.session_state.get("logged_in", False):
        st.warning("Please login first.")
        st.session_state.page = "login"
        st.rerun()

    user = st.session_state.user

    # ---------------- Page Header ----------------

    st.title("📊 FutureFund AI Dashboard")

    st.caption(
        "Your personal investment command center for smarter financial decisions."
    )

    st.markdown("---")

    # ---------------- Welcome Banner ----------------

    with st.container(border=True):

        st.markdown(
            f"""
### 👋 Welcome back, **{user[1]}**

Stay consistent with your investments today to build a stronger tomorrow.
"""
        )

    st.markdown("")

    # ---------------- Financial Score ----------------

    score_data = calculate_financial_score(
        income=user[5],
        savings=user[8],
        risk=user[6],
        goal=user[9]
    )

    monthly_savings = user[8]

    estimated_net_worth = monthly_savings * 24

    recommended_sip = max(
        monthly_savings * 0.60,
        1000
    )

    # Portfolio used across dashboard

    portfolio = {
        "Equity": 50,
        "Debt": 30,
        "Gold": 10,
        "Cash": 10
    }

    # ---------------- Profile Overview ----------------

    st.subheader("👤 Profile Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Age",
            f"{user[4]} Years"
        )

    with c2:
        st.metric(
            "Monthly Income",
            f"₹{user[5]:,.0f}"
        )

    with c3:
        st.metric(
            "Monthly Savings",
            f"₹{monthly_savings:,.0f}"
        )

    with c4:
        st.metric(
            "Risk Profile",
            user[6]
        )

    st.markdown("")

    left, right = st.columns([2, 1])

    with left:

        st.info(
            f"""
**Email**

{user[2]}

**Financial Goal**

{user[9]}
"""
        )

    with right:

        st.metric(
            "Financial Health Score",
            f"{score_data['score']}/100"
        )

    st.markdown("---")

    # ---------------- Analytics Dashboard ----------------

    st.subheader("📈 Financial Snapshot")

    show_analytics_dashboard(
        financial_score=score_data["score"],
        monthly_savings=monthly_savings,
        estimated_net_worth=estimated_net_worth,
        recommended_sip=recommended_sip
    )

    # ---------------- Interactive Charts ----------------

    show_financial_charts(
        monthly_savings=monthly_savings,
        recommended_sip=recommended_sip,
        financial_score=score_data["score"],
        portfolio=portfolio
    )

    st.markdown("---")

    # ---------------- Financial Health ----------------

    st.subheader("⭐ Financial Health Analysis")

    score_col, message_col = st.columns([1, 2])

    with score_col:

        st.metric(
            "Overall Score",
            f"{score_data['score']}/100"
        )

    with message_col:

        if score_data["score"] >= 80:

            st.success(
                "Excellent! Your financial health is in a strong position."
            )

        elif score_data["score"] >= 60:

            st.info(
                "Good progress. A few improvements can strengthen your finances."
            )

        else:

            st.warning(
                "Let's improve your financial foundation with better saving habits."
            )

    col1, col2 = st.columns(2)

    with col1:

        st.success("### ✅ Financial Strengths")

        if score_data["strengths"]:

            for item in score_data["strengths"]:
                st.write(f"• {item}")

        else:

            st.write("No strengths identified yet.")

    with col2:

        st.warning("### 📌 Suggested Improvements")

        if score_data["improvements"]:

            for item in score_data["improvements"]:
                st.write(f"• {item}")

        else:

            st.write(
                "You're doing great! Keep investing consistently."
            )

    st.markdown("---")

    # ---------------- Investment Simulator ----------------

    st.subheader("💰 Investment Tools")

    show_investment_simulator()

    st.markdown("---")

    # ---------------- Portfolio Allocation ----------------

    st.subheader("📊 Portfolio Allocation")

    show_portfolio_allocator()

    st.markdown("---")

    # ---------------- AI Financial Advisor ----------------

    st.subheader("🤖 AI Financial Advisor")

    show_financial_advisor()

    st.markdown("---")

    # ---------------- Financial Report ----------------

    st.subheader("📄 Download Financial Report")

    st.write(
        "Generate a professional PDF summary of your financial profile and investment recommendations."
    )

    pdf = generate_financial_report(user)

    st.download_button(
        label="⬇ Download PDF Report",
        data=pdf,
        file_name="FutureFund_AI_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.markdown("---")

    # ---------------- Investment History ----------------

    history = get_history(user[0]) or []

    csv_file = history_to_csv(history)
    excel_file = history_to_excel(history)

    st.subheader("📁 Export Investment History")

    export_col1, export_col2 = st.columns(2)

    with export_col1:

        st.download_button(
            label="⬇ Download CSV",
            data=csv_file,
            file_name="FutureFund_History.csv",
            mime="text/csv",
            use_container_width=True
        )

    with export_col2:

        st.download_button(
            label="⬇ Download Excel",
            data=excel_file,
            file_name="FutureFund_History.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    st.markdown("---")

    # ---------------- Recent Activity ----------------

    st.subheader("🕒 Recent Activity")

    if history:

        for feature, result, created_at in history:

            with st.container(border=True):

                st.markdown(f"#### {feature}")

                st.write(result)

                st.caption(f"Generated on: {created_at}")

    else:

        st.info(
            "No investment history found yet. Start using FutureFund AI to build your financial journey."
        )