import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def show_financial_charts(
    monthly_savings,
    recommended_sip,
    financial_score,
    portfolio
):
    st.subheader("📊 Financial Insights")

    # -----------------------------
    # SIP Growth Projection
    # -----------------------------

    years = list(range(1, 11))
    annual_return = 0.12

    values = []

    corpus = 0

    for year in years:

        for _ in range(12):
            corpus = corpus * (1 + annual_return / 12)
            corpus += recommended_sip

        values.append(round(corpus))

    sip_df = pd.DataFrame({
        "Year": years,
        "Corpus": values
    })

    fig = px.line(
        sip_df,
        x="Year",
        y="Corpus",
        markers=True,
        title="Projected SIP Growth"
    )

    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Portfolio Pie Chart
    # -----------------------------

    if portfolio:

        pie = px.pie(
            names=list(portfolio.keys()),
            values=list(portfolio.values()),
            title="Recommended Portfolio Allocation"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    # -----------------------------
    # Monthly Savings
    # -----------------------------

    savings_df = pd.DataFrame({
        "Category": ["Savings", "Recommended SIP"],
        "Amount": [
            monthly_savings,
            recommended_sip
        ]
    })

    bar = px.bar(
        savings_df,
        x="Category",
        y="Amount",
        text="Amount",
        title="Monthly Savings Overview"
    )

    bar.update_layout(height=350)

    st.plotly_chart(
        bar,
        use_container_width=True
    )

    # -----------------------------
    # Financial Score Gauge
    # -----------------------------

    gauge = go.Figure(

        go.Indicator(
            mode="gauge+number",
            value=financial_score,
            title={"text": "Financial Health Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"thickness": 0.35},
                "steps": [
                    {"range": [0, 40], "color": "#ffb3b3"},
                    {"range": [40, 70], "color": "#ffe680"},
                    {"range": [70, 100], "color": "#b6f2c6"},
                ],
            },
        )
    )

    gauge.update_layout(height=350)

    st.plotly_chart(
        gauge,
        use_container_width=True
    )