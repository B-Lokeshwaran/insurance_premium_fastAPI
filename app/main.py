from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import auth, policy, premium, payment


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Insurance Premium Payment API")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(policy.router, prefix="/policies", tags=["Policies"])
app.include_router(premium.router, prefix="/premium", tags=["Premium"])
app.include_router(payment.router, prefix="/payments", tags=["Payments"])