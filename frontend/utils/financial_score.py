def calculate_financial_score(
    income,
    savings,
    risk,
    goal
):
    score = 0
    strengths = []
    improvements = []

    # -----------------------------
    # Savings Rate (40 points)
    # -----------------------------
    if income > 0:
        savings_rate = (savings / income) * 100
    else:
        savings_rate = 0

    if savings_rate >= 30:
        score += 40
        strengths.append("Excellent savings rate.")
    elif savings_rate >= 20:
        score += 30
        strengths.append("Good savings habit.")
    elif savings_rate >= 10:
        score += 20
        improvements.append("Try to increase your monthly savings.")
    else:
        score += 10
        improvements.append("Your savings rate is quite low.")

    # -----------------------------
    # Income (20 points)
    # -----------------------------
    if income >= 100000:
        score += 20
    elif income >= 50000:
        score += 15
    elif income >= 25000:
        score += 10
    else:
        score += 5
        improvements.append("Focus on increasing your income over time.")

    # -----------------------------
    # Risk Appetite (20 points)
    # -----------------------------
    if risk == "Medium":
        score += 20
        strengths.append("Balanced risk profile.")
    elif risk == "High":
        score += 15
        strengths.append("Comfortable with market volatility.")
    else:
        score += 10
        improvements.append("Consider learning more about long-term investing.")

    # -----------------------------
    # Financial Goal (20 points)
    # -----------------------------
    if goal in ["Retirement", "Wealth Creation"]:
        score += 20
    else:
        score += 15

    return {
        "score": score,
        "strengths": strengths,
        "improvements": improvements
    }