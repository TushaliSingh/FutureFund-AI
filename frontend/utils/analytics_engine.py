import pandas as pd


def generate_sample_sip_growth():
    """
    Generate sample yearly SIP growth data.

    NOTE:
    Placeholder data for dashboard development.
    """

    years = list(range(1, 11))

    investment = [
        120000, 240000, 360000, 480000, 600000,
        720000, 840000, 960000, 1080000, 1200000
    ]

    portfolio = [
        126000, 268000, 430000, 617000, 832000,
        1080000, 1365000, 1690000, 2060000, 2480000
    ]

    return pd.DataFrame({
        "Year": years,
        "Investment": investment,
        "Portfolio Value": portfolio
    })


def generate_sample_portfolio():
    """
    Sample portfolio allocation.

    Later this will be replaced with
    real portfolio allocation generated
    by the recommendation engine.
    """

    return pd.DataFrame({
        "Asset": [
            "Equity",
            "Debt",
            "Gold",
            "Emergency Fund"
        ],
        "Allocation": [
            60,
            25,
            10,
            5
        ]
    })
def generate_sample_goal_progress():
    """
    Sample goal progress data.

    This will later be replaced by
    real goal planning calculations.
    """

    return {
        "goal_name": "Dream Home",
        "current_amount": 1200000,
        "target_amount": 2500000,
        "progress": 48
    }
def generate_sample_wealth_projection():
    """
    Sample future wealth projection.

    Placeholder data for dashboard
    development. This will later use
    the investment engine.
    """

    return pd.DataFrame({
        "Year": [
            "2026",
            "2027",
            "2028",
            "2029",
            "2030"
        ],
        "Projected Wealth": [
            450000,
            720000,
            1050000,
            1480000,
            2000000
        ]
    })