from pydantic import BaseModel


class PolicyCreate(BaseModel):
    name: str
    base_amount: float
    risk_factor: float