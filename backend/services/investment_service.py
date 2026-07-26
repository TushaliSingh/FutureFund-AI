"""
Investment related business logic.
"""


def calculate_sip(
    monthly_investment: float,
    annual_return: float,
    years: int,
):
    """
    Calculate SIP maturity value.
    """

    months = years * 12
    monthly_rate = annual_return / (12 * 100)

    # Handle 0% return separately
    if monthly_rate == 0:
        maturity_value = monthly_investment * months
    else:
        maturity_value = (
            monthly_investment
            * (
                ((1 + monthly_rate) ** months - 1)
                / monthly_rate
            )
            * (1 + monthly_rate)
        )

    invested_amount = monthly_investment * months

    estimated_returns = maturity_value - invested_amount

    return {
        "invested_amount": round(invested_amount, 2),
        "estimated_returns": round(estimated_returns, 2),
        "maturity_value": round(maturity_value, 2),
    }