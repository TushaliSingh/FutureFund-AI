from utils.investment_engine import sip_calculator


result = sip_calculator(
    monthly_investment=5000,
    annual_return=12,
    years=20
)

print(result)