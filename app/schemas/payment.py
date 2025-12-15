from pydantic import BaseModel


class PaymentCreate(BaseModel):
    policy_id: int
    amount: float
