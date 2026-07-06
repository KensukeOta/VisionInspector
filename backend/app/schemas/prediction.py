from pydantic import BaseModel


class PredictionResponse(BaseModel):
    model: str
    score: float
    label: bool
    message: str
    description: str
    overlay_url: str
    processing_time_ms: float
