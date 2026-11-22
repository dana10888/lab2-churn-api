
from pathlib import Path
import json
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Find the project root
ROOT = Path(__file__).resolve().parents[2]
MODEL_DIR = Path(__import__("os").getenv("MODEL_DIR", str(ROOT)))
MODEL_PATH = MODEL_DIR / "model.joblib"

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
    metadata_path = MODEL_DIR / "metadata.json"

    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        version = metadata.get("model_version", "unknown")
    else:
        version = "local"

    return {
        "status": "ok",
        "model_version": version
    }


@app.post("/predict")
def predict(customer: CustomerInput):
    data = pd.DataFrame([customer.model_dump()]) 

    if "monthly_charges" in model.feature_names_in_:
        data = data.rename(columns={"monthly_fee": "monthly_charges"})


    probability = float(model.predict_proba(data)[0, 1])

    return {
        "churn_probability": round(probability, 3)
    }
