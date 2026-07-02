from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PredictionResult:
    model: str
    score: float
    label: bool
    overlay_path: str
