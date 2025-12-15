from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate

router = APIRouter()


@router.post("/")
def make_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = Payment(
        policy_id=payment.policy_id,
        amount=payment.amount,
        status="SUCCESS",
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment) 
    return db_payment
