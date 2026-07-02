from pathlib import Path

from fastapi.testclient import TestClient

from app.dependencies import get_inference_service
from app.main import app


class DummyInferenceService:
    def predict(self, image_path: Path) -> dict:
        return {
            "score": 0.95,
            "label": True,
            "overlay_path": "outputs/test.png",
        }


def override_service() -> DummyInferenceService:
    return DummyInferenceService()


app.dependency_overrides[get_inference_service] = override_service

client = TestClient(app)


def test_predict() -> None:
    files = {
        "file": ("test.png", b"fake image", "image/png"),
    }

    response = client.post("/predict?model=padim", files=files)

    assert response.status_code == 200

    body = response.json()

    assert body["model"] == "padim"
    assert body["score"] == 0.95
    assert body["label"] is True
    assert body["message"] == "Anomaly detected"
    assert body["overlay_url"] == "/outputs/test.png"
    assert isinstance(body["processing_time_ms"], float)


def test_predict_rejects_unsupported_model() -> None:
    files = {
        "file": ("test.png", b"fake image", "image/png"),
    }

    response = client.post("/predict?model=patchcore", files=files)

    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported model: patchcore"


def test_predict_rejects_unsupported_file_type() -> None:
    files = {
        "file": ("test.txt", b"fake text", "text/plain"),
    }

    response = client.post("/predict?model=padim", files=files)

    assert response.status_code == 400
