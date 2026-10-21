from contextlib import asynccontextmanager
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model

    model = joblib.load(
        "insurance_model.pkl"
    )

    yield

    model = None


app = FastAPI(
    title="Insurance Charges Prediction API",
    description=(
        "Predict medical insurance charges "
        "using a machine-learning model."
    ),
    version="1.0.0",
    lifespan=lifespan
)


class InsuranceInput(BaseModel):
    age: int = Field(
        ge=18,
        le=100
    )

    sex: Literal[
        "male",
        "female"
    ]

    bmi: float = Field(
        ge=10,
        le=70
    )

    children: int = Field(
        ge=0,
        le=10
    )

    smoker: Literal[
        "yes",
        "no"
    ]

    region: Literal[
        "southwest",
        "southeast",
        "northwest",
        "northeast"
    ]


@app.get("/")
def home():
    return {
        "message": (
            "Insurance prediction API "
            "is running"
        ),
        "documentation": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post("/predict")
def predict_charges(data: InsuranceInput):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is unavailable"
        )

    input_data = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker,
        "region": data.region
    }])

    prediction = model.predict(
        input_data
    )[0]

    prediction = max(
        float(prediction),
        0
    )

    return {
        "input": data.model_dump(),
        "predicted_charge": round(
            prediction,
            2
        ),
        "note": (
            "Educational prediction only; "
            "not an official insurance quote."
        )
    }