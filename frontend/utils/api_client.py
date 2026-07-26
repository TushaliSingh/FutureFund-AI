import requests


BASE_URL = "https://futurefund-ai.onrender.com/api/v1"


# -------------------------
# SIP Calculator
# -------------------------

def calculate_sip(
    monthly_investment,
    annual_return,
    years,
):
    response = requests.post(
        f"{BASE_URL}/investments/sip",
        json={
            "monthly_investment": monthly_investment,
            "annual_return": annual_return,
            "years": years,
        },
    )

    response.raise_for_status()

    return response.json()


# -------------------------
# Lump Sum Calculator
# -------------------------

def calculate_lumpsum(
    principal,
    annual_return,
    years,
):
    response = requests.post(
        f"{BASE_URL}/investments/lumpsum",
        json={
            "principal": principal,
            "annual_return": annual_return,
            "years": years,
        },
    )

    response.raise_for_status()

    return response.json()
