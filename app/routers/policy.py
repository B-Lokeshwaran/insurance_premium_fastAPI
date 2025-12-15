from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.policy import Policy
from app.schemas.policy import PolicyCreate

router = APIRouter()


@router.post("/")
def create_policy(policy: PolicyCreate, db: Session = Depends(get_db)):
    db_policy = Policy(**policy.dict())
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy) 
    return db_policy


@router.get("/")
def list_policies(db: Session = Depends(get_db)):
    return db.query(Policy).all()
