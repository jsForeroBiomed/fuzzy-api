from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_predict_endpoint():
    payload = {
        "presion_sistolica": 150,
        "colesterol_total": 162,
        "indice_masa_corporal": 26,
        "edad": 27,
        "actividad_fisica": 6,
        "cigarrillos_por_dia": 4
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    json_response = response.json()
    assert isinstance(json_response, dict)

    assert "riesgo_cardiovascular" in json_response

    assert isinstance(json_response["riesgo_cardiovascular"], (float, int))
