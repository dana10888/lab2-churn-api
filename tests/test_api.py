
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_loading():
    from src.app.main import model

    assert model is not None
    assert hasattr(model, "predict_proba")



def test_invalid_input():
    customer = {
        "tenure_months": -5,
        "monthly_fee": 75.0,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_edge_case():
    customer = {
        "tenure_months": 0,
        "monthly_fee": 0.0,
        "contract": "month-to-month",
        "internet_service": "none",
        "support_calls": 0
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200

    probability = response.json()["churn_probability"]
    assert 0 <= probability <= 1



def test_prediction_consistency():
    customer = {
        "tenure_months": 12,
        "monthly_fee": 75.0,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3
    }

    response1 = client.post("/predict", json=customer)
    response2 = client.post("/predict", json=customer)

    assert response1.status_code == 200
    assert response2.status_code == 200

    probability1 = response1.json()["churn_probability"]
    probability2 = response2.json()["churn_probability"]

    assert probability1 == probability2
