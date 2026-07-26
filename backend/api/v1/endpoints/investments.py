from fastapi import APIRouter

from backend.schemas import SIPRequest, SIPResponse
from backend.services import calculate_sip


router = APIRouter(
    prefix="/investments",
    tags=["Investments"],
)


@router.post(
    "/sip",
    response_model=SIPResponse,
)
def calculate_sip_api(request: SIPRequest):
    """
    Calculate SIP maturity value.
    """

    result = calculate_sip(
        monthly_investment=request.monthly_investment,
        annual_return=request.annual_return,
        years=request.years,
    )

    return SIPResponse(
        invested_amount=result["invested_amount"],
        estimated_returns=result["estimated_returns"],
        maturity_value=result["maturity_value"],
    )