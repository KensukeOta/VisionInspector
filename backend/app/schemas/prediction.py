from pydantic import BaseModel


class PredictionResponse(BaseModel):
    score: float
    label: bool
    message: str
    overlay_url: str
