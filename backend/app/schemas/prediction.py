from typing import Annotated

from fastapi import Query
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    model: Annotated[str, Query()] = "padim"
    score: float
    label: bool
    message: str
    overlay_url: str
    processing_time_ms: float
