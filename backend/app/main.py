from fastapi import FastAPI

from app.api.auth.routes import router as auth_router

app = FastAPI(
    title="ABVRS ERP API",
    version="1.0.0",
    description="Atal Bihari Vajpayee Residential School ERP Backend"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ABVRS ERP API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }