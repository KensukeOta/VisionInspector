from functools import lru_cache

from app.services.inference_service import InferenceService


@lru_cache(maxsize=1)
def get_inference_service() -> InferenceService:
    return InferenceService(model_name="padim")
