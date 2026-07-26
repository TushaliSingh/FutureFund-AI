import math


# ------------------------------------------
# SIP Calculator
# ------------------------------------------

def sip_calculator(monthly_investment, annual_return, years):

    monthly_rate = annual_return / 12 / 100
    months = years * 12

    maturity_value = monthly_investment * (
        (((1 + monthly_rate) ** months - 1) / monthly_rate)
        * (1 + monthly_rate)
    )

    invested_amount = monthly_investment * months
    estimated_returns = maturity_value - invested_amount

    return {
        "invested_amount": invested_amount,
        "estimated_returns": estimated_returns,
        "maturity_value": maturity_value,
    }


# ------------------------------------------
# Lump Sum Calculator
# ------------------------------------------

def lumpsum_calculator(principal, annual_return, years):

    maturity_value = principal * ((1 + annual_return / 100) ** years)

    estimated_returns = maturity_value - principal

    return {
        "invested_amount": principal,
        "estimated_returns": estimated_returns,
        "maturity_value": maturity_value,
    }


# ------------------------------------------
# Goal Planner
# ------------------------------------------

def goal_sip_calculator(target_amount, annual_return, years):

    monthly_rate = annual_return / 12 / 100
    months = years * 12

    required_sip = target_amount / (
        (((1 + monthly_rate) ** months - 1) / monthly_rate)
        * (1 + monthly_rate)
    )

    invested_amount = required_sip * months

    return {
        "required_monthly_sip": required_sip,
        "invested_amount": invested_amount,
        "target_amount": target_amount,
    }


# ------------------------------------------
# Inflation Calculator
# ------------------------------------------

def inflation_calculator(current_amount, inflation_rate, years):

    future_value = current_amount * (
        (1 + inflation_rate / 100) ** years
    )

    return {
        "future_value": future_value,
    }


# ------------------------------------------
# CAGR Calculator
# ------------------------------------------

def cagr_calculator(initial_value, final_value, years):

    cagr = (
        (final_value / initial_value) ** (1 / years) - 1
    ) * 100

    return {
        "cagr": cagr,
    }


# ------------------------------------------
# Portfolio Allocation
# ------------------------------------------

def portfolio_allocation(age, risk_level):

    risk_level = risk_level.lower()

    if age < 30:

        if risk_level == "low":
            return {
                "Equity": 45,
                "Debt": 45,
                "Gold": 10,
            }

        elif risk_level == "medium":
            return {
                "Equity": 70,
                "Debt": 20,
                "Gold": 10,
            }

        else:
            return {
                "Equity": 85,
                "Debt": 5,
                "Gold": 10,
            }

    elif age < 50:

        if risk_level == "low":
            return {
                "Equity": 35,
                "Debt": 55,
                "Gold": 10,
            }

        elif risk_level == "medium":
            return {
                "Equity": 60,
                "Debt": 30,
                "Gold": 10,
            }

        else:
            return {
                "Equity": 75,
                "Debt": 15,
                "Gold": 10,
            }

    else:

        if risk_level == "low":
            return {
                "Equity": 20,
                "Debt": 70,
                "Gold": 10,
            }

        elif risk_level == "medium":
            return {
                "Equity": 45,
                "Debt": 45,
                "Gold": 10,
            }

        else:
            return {
                "Equity": 60,
                "Debt": 30,
                "Gold": 10,
            }