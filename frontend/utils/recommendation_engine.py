def generate_recommendation(
    income,
    expenses,
    savings,
    risk,
    goal,
    experience
):
    """
    Rule-based financial recommendation engine.

    Returns:
        {
            "sip": int,
            "portfolio": dict,
            "strategy": list,
            "improvements": list
        }
    """

    # --------------------------------------------------
    # Financial Ratios
    # --------------------------------------------------

    savings_rate = savings / income if income > 0 else 0
    expense_ratio = expenses / income if income > 0 else 0

    # --------------------------------------------------
    # Suggested SIP
    # --------------------------------------------------

    if savings_rate >= 0.40:
        sip_percentage = 0.70

    elif savings_rate >= 0.30:
        sip_percentage = 0.60

    elif savings_rate >= 0.20:
        sip_percentage = 0.50

    else:
        sip_percentage = 0.40

    suggested_sip = max(
        round(savings * sip_percentage),
        1000
    )

    # --------------------------------------------------
    # Portfolio Allocation
    # --------------------------------------------------

    if risk.lower() == "high":

        portfolio = {
            "Equity": 80,
            "Debt": 10,
            "Gold": 10
        }

    elif risk.lower() == "medium":

        portfolio = {
            "Equity": 60,
            "Debt": 30,
            "Gold": 10
        }

    else:

        portfolio = {
            "Equity": 40,
            "Debt": 50,
            "Gold": 10
        }

    # Slight adjustment based on age/experience
    if experience.lower() == "beginner":

        portfolio["Equity"] = max(
            portfolio["Equity"] - 10,
            30
        )

        portfolio["Debt"] += 10

    elif experience.lower() == "advanced":

        portfolio["Equity"] = min(
            portfolio["Equity"] + 5,
            90
        )

        portfolio["Debt"] = max(
            portfolio["Debt"] - 5,
            5
        )

    # --------------------------------------------------
    # Investment Strategy
    # --------------------------------------------------

    strategy = []

    strategy.append(
        f"Invest approximately ₹{suggested_sip:,} every month through disciplined SIPs."
    )

    if goal == "Retirement":

        strategy.append(
            "Maintain a long-term investment horizon and increase SIPs as your income grows."
        )

    elif goal == "House":

        strategy.append(
            "Balance wealth creation with capital preservation to prepare for a future home purchase."
        )

    elif goal == "Education":

        strategy.append(
            "Focus on consistent investing while gradually reducing risk as the goal approaches."
        )

    elif goal == "Emergency Fund":

        strategy.append(
            "Build 6–12 months of essential expenses before increasing exposure to equity investments."
        )

    else:

        strategy.append(
            "Maintain a diversified portfolio and review your investments at least once a year."
        )

    if savings_rate >= 0.30:

        strategy.append(
            "Your savings habit is strong. Continue increasing investments whenever your salary increases."
        )

    else:

        strategy.append(
            "Improve your monthly savings rate to accelerate long-term wealth creation."
        )

    # --------------------------------------------------
    # Improvements
    # --------------------------------------------------

    improvements = []

    if expense_ratio > 0.70:

        improvements.append(
            "Your expenses exceed 70% of your income. Reducing discretionary spending can improve your financial stability."
        )

    if savings_rate < 0.20:

        improvements.append(
            "Aim to save at least 20% of your monthly income."
        )

    if experience.lower() == "beginner":

        improvements.append(
            "Start with diversified index funds before exploring sector-specific investments."
        )

    if risk.lower() == "high":

        improvements.append(
            "Review your portfolio annually to ensure your risk level still matches your financial goals."
        )

    if income < 50000:

        improvements.append(
            "As your income increases, prioritize increasing your SIP amount rather than lifestyle expenses."
        )

    if not improvements:

        improvements.append(
            "Excellent financial profile. Stay consistent and review your portfolio every 6–12 months."
        )

    # --------------------------------------------------
    # Return Recommendation
    # --------------------------------------------------

    return {
        "sip": suggested_sip,
        "portfolio": portfolio,
        "strategy": strategy,
        "improvements": improvements
    }