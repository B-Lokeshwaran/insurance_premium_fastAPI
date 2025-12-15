from fastapi import APIRouter
from app.services.premium_calculator import calculate_premium

router = APIRouter()


@router.get("/calculate")
def calculate(base_amount: float, age: int, risk_factor: float):
    premium = calculate_premium(base_amount, age, risk_factor)
    return {"premium": premium}
