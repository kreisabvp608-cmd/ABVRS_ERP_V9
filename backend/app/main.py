from fastapi import FastAPI

app = FastAPI(
    title="ABVRS ERP API",
    version="1.0.0",
    description="Atal Bihari Vajpayee Residential School ERP Backend"
)


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