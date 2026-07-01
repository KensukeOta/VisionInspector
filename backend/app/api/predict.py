from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile

from app.dependencies import get_inference_service
from app.schemas.prediction import PredictionResponse
from app.services.inference_service import InferenceService

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(
    file: Annotated[
        UploadFile,
        File(...),
    ],
    inference_service: Annotated[
        InferenceService,
        Depends(get_inference_service),
    ],
) -> PredictionResponse:
    suffix = Path(file.filename or "").suffix or ".png"

    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = Path(tmp.name)

    result = inference_service.predict(tmp_path)

    label = result["label"]
    message = "Anomaly detected" if label else "Normal image"

    overlay_path = Path(result["overlay_path"])
    overlay_url = f"/outputs/{overlay_path.name}"

    return PredictionResponse(
        score=result["score"],
        label=label,
        message=message,
        overlay_url=overlay_url,
    )
