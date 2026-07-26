from utils.financial_score import calculate_financial_score
from utils.recommendation_engine import generate_recommendation


def generate_financial_analysis(user):

    financial_score = calculate_financial_score(
        income=user[5],
        savings=user[8],
        risk=user[6],
        goal=user[9]
    )

    recommendation = generate_recommendation(
        income=user[5],
        expenses=user[7],
        savings=user[8],
        risk=user[6],
        goal=user[9],
        experience=user[10]
    )

    return {
        "financial_score": financial_score,
        "recommendation": recommendation
    }