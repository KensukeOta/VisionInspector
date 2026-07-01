from pathlib import Path

from fastapi.testclient import TestClient

from app.dependencies import get_inference_service
from app.main import app


class DummyInferenceService:
    def predict(self, image_path: Path):
        return {
            "score": 0.95,
            "label": True,
            "overlay_path": "outputs/test.png",
        }


def override_service():
    return DummyInferenceService()


app.dependency_overrides[get_inference_service] = override_service

client = TestClient(app)


def test_predict():
    files = {
        "file": ("test.png", b"fake image", "image/png"),
    }

    response = client.post("/predict", files=files)

    assert response.status_code == 200

    body = response.json()

    assert body["score"] == 0.95
    assert body["label"] is True
    assert body["message"] == "Anomaly detected"
