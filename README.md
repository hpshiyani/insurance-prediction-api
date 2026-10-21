# Insurance Price Prediction API

A machine-learning API that predicts estimated insurance charges using age, sex, BMI, number of children, smoking status, and region.

## Live API

Base URL:

```text
https://YOUR-RENDER-URL.onrender.com
```

Interactive API documentation:

```text
https://YOUR-RENDER-URL.onrender.com/docs
```

## API Endpoints

### 1. Check API

```http
GET /
```

Example response:

```json
{
  "message": "Insurance prediction API is running",
  "documentation": "/docs"
}
```

### 2. Health Check

```http
GET /health
```

### 3. Predict Insurance Charges

```http
POST /predict
```

Request body:

```json
{
  "age": 45,
  "sex": "female",
  "bmi": 31.2,
  "children": 2,
  "smoker": "yes",
  "region": "southeast"
}
```

Example response:

```json
{
  "input": {
    "age": 45,
    "sex": "female",
    "bmi": 31.2,
    "children": 2,
    "smoker": "yes",
    "region": "southeast"
  },
  "predicted_charge": 42173.56,
  "note": "Educational prediction only; not an official insurance quote."
}
```

## How to Test Using Swagger UI

1. Open `https://YOUR-RENDER-URL.onrender.com/docs`.
2. Select the `POST /predict` endpoint.
3. Click **Try it out**.
4. Enter the patient details in JSON format.
5. Click **Execute**.
6. The predicted insurance charge will appear under **Response body**.

## Test Using Python

```python
import requests

url = "https://YOUR-RENDER-URL.onrender.com/predict"

data = {
    "age": 45,
    "sex": "female",
    "bmi": 31.2,
    "children": 2,
    "smoker": "yes",
    "region": "southeast"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

Open the documentation:

```text
http://127.0.0.1:8000/docs
```

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Joblib
- Render

## Disclaimer

This project is created for educational purposes. Its predictions are not official insurance quotations.
