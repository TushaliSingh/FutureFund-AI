import streamlit as st
import plotly.graph_objects as go

from utils.analytics_engine import (
    generate_sample_sip_growth,
    generate_sample_portfolio,
    generate_sample_goal_progress,
    generate_sample_wealth_projection
)
from utils.report_generator import FinancialReportGenerator


def show_analytics_dashboard(
    financial_score,
    monthly_savings,
    estimated_net_worth,
    recommended_sip
):
    """
    Displays the financial analytics dashboard.

    This component is responsible only for presenting
    analytics data. All calculations should come from
    dedicated utility modules.
    """

    st.subheader("📊 Financial Analytics Dashboard")

    # ==========================================================
    # KPI CARDS
    # ==========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="💰 Estimated Portfolio Value",
            value=f"₹{estimated_net_worth:,.0f}"
        )

    with col2:
        st.metric(
            label="💵 Monthly Savings",
            value=f"₹{monthly_savings:,.0f}"
        )

    with col3:
        st.metric(
            label="📈 Financial Health",
            value=f"{financial_score}/100"
        )

    with col4:
        st.metric(
            label="🎯 Recommended SIP",
            value=f"₹{recommended_sip:,.0f}"
        )

    st.divider()

    # ==========================================================
    # SIP GROWTH CHART
    # ==========================================================

    st.subheader("📈 SIP Growth Projection")

    df = generate_sample_sip_growth()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Investment"],
            mode="lines+markers",
            name="Total Investment"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Portfolio Value"],
            mode="lines+markers",
            name="Portfolio Value"
        )
    )

    fig.update_layout(
        title="Investment Growth Over Time",
        xaxis_title="Years",
        yaxis_title="Amount (₹)",
        hovermode="x unified",
        template="plotly_white",
        height=500,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # PORTFOLIO ALLOCATION
    # ==========================================================

    st.subheader("🥧 Portfolio Allocation")

    portfolio_df = generate_sample_portfolio()

    pie_fig = go.Figure(
        data=[
            go.Pie(
                labels=portfolio_df["Asset"],
                values=portfolio_df["Allocation"],
                hole=0.45
            )
        ]
    )

    pie_fig.update_layout(
        title="Recommended Portfolio Distribution",
        template="plotly_white",
        height=500,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # FINANCIAL HEALTH GAUGE
    # ==========================================================

    st.subheader("🏆 Financial Health Gauge")

    gauge_fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=financial_score,
            title={"text": "Overall Financial Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#fff3cd"},
                    {"range": [70, 100], "color": "#d4edda"},
                ],
            },
        )
    )

    gauge_fig.update_layout(
        template="plotly_white",
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        gauge_fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # GOAL PROGRESS
    # ==========================================================

    st.subheader("🎯 Goal Progress")

    goal = generate_sample_goal_progress()

    st.write(f"**Goal:** {goal['goal_name']}")

    st.progress(goal["progress"] / 100)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Savings",
            f"₹{goal['current_amount']:,.0f}"
        )

    with col2:
        st.metric(
            "Target Amount",
            f"₹{goal['target_amount']:,.0f}"
        )

    with col3:
        remaining = goal["target_amount"] - goal["current_amount"]

        st.metric(
            "Remaining",
            f"₹{remaining:,.0f}"
        )

    st.divider()

    # ==========================================================
    # WEALTH PROJECTION
    # ==========================================================

    st.subheader("📅 Wealth Projection")

    wealth_df = generate_sample_wealth_projection()

    wealth_fig = go.Figure()

    wealth_fig.add_trace(
        go.Bar(
            x=wealth_df["Year"],
            y=wealth_df["Projected Wealth"],
            text=wealth_df["Projected Wealth"],
            textposition="outside",
            name="Projected Wealth"
        )
    )

    wealth_fig.update_layout(
        title="Estimated Wealth Over the Next 5 Years",
        xaxis_title="Year",
        yaxis_title="Projected Wealth (₹)",
        template="plotly_white",
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        wealth_fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # FINANCIAL REPORT
    # ==========================================================

    st.subheader("📄 Download Financial Report")

    report_data = {
    "username": st.session_state.get("username", "User"),
    "estimated_net_worth": estimated_net_worth,
    "monthly_savings": monthly_savings,
    "financial_score": financial_score,
    "recommended_sip": recommended_sip,
    "recommendation": st.session_state.get("latest_recommendation"),
    }

    generator = FinancialReportGenerator()

    pdf = generator.generate_report(report_data)

    st.download_button(
        label="📥 Download PDF Report",
        data=pdf,
        file_name="FutureFund_AI_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )