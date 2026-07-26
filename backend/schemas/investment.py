from pydantic import BaseModel, Field


class SIPRequest(BaseModel):
    """
    Request model for SIP calculation API.
    """

    monthly_investment: float = Field(
        ...,
        gt=0,
        description="Monthly SIP investment amount"
    )

    annual_return: float = Field(
        ...,
        gt=0,
        description="Expected annual return percentage"
    )

    years: int = Field(
        ...,
        gt=0,
        description="Investment duration in years"
    )


from pydantic import BaseModel


class SIPResponse(BaseModel):
    invested_amount: float
    estimated_returns: float
    maturity_value: float