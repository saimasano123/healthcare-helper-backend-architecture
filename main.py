from fastapi import FastAPI
from routers import insurance  # This will be your routes module

app = FastAPI(
    title="Healthcare AI Assistant Backend",
    description="API backend for insurance analysis and cost comparison",
    version="1.0"
)

app.include_router(insurance.router, prefix="/api/insurance", tags=["Insurance"])

@app.get("/")
def root():
    return {"message": "Backend is working!"}
