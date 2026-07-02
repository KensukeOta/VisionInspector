from app.services.inference_service import InferenceService


def get_inference_service() -> InferenceService:
    return InferenceService(model_name="padim")
