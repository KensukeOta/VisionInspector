import time
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.dependencies import get_inference_service
from app.schemas.prediction import PredictionResponse
from app.services.inference_service import InferenceService

router = APIRouter()

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


@router.post("/predict", response_model=PredictionResponse)
async def predict(
    inference_service: Annotated[
        InferenceService,
        Depends(get_inference_service),
    ],
    file: Annotated[UploadFile, File(...)],
    model: Annotated[str, Query()] = "padim",
) -> PredictionResponse:
    start_time = time.perf_counter()

    if model != "padim":
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported model: {model}",
        )

    suffix = Path(file.filename or "").suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload jpg, jpeg, png, or webp.",
        )

    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = Path(tmp.name)

    try:
        result = inference_service.predict(tmp_path)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed.",
        ) from exc

    label = result["label"]
    message = "Anomaly detected" if label else "Normal image"

    overlay_path = Path(result["overlay_path"])
    overlay_url = f"/outputs/{overlay_path.name}"

    processing_time_ms = (time.perf_counter() - start_time) * 1000

    return PredictionResponse(
        model=model,
        score=result["score"],
        label=label,
        message=message,
        overlay_url=overlay_url,
        processing_time_ms=round(processing_time_ms, 2),
    )
