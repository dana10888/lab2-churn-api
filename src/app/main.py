
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Find the project root
ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "model.joblib"

# Load trained model
model = joblib.load(MODEL_PATH)

# Create FastAPI application
app = FastAPI(title="AI381 Lab 2 Churn API")


# Validate customer input
class CustomerInput(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_fee: float = Field(ge=0)
    contract: Literal["month-to-month", "one-year", "two-year"]
    internet_service: Literal["fiber", "none", "dsl"]
    support_calls: int = Field(ge=0)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: CustomerInput):
    data = pd.DataFrame([customer.model_dump()])

    probability = float(model.predict_proba(data)[0, 1])

    return {
        "churn_probability": round(probability, 3)
    }
