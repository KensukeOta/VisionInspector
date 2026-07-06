from pathlib import Path
from typing import Any, cast

import cv2
import numpy as np
from anomalib.engine import Engine

from app.core.config import OUTPUT_DIR
from app.core.model_names import ModelName
from app.schemas.prediction_result import PredictionResult
from app.services.model_loader import model_loader
from app.utils.image_utils import (
    create_overlay,
    load_rgb_image,
    save_overlay_image,
)


class InferenceService:
    def __init__(self, model_name: ModelName = "padim") -> None:
        self.model_name = model_name
        self.model = model_loader.get(model_name)
        self.engine = Engine(
            accelerator="cpu",
            devices=1,
        )

    def predict(self, image_path: Path) -> PredictionResult:
        image = load_rgb_image(image_path)
        original_np = np.array(image)

        predictions = self.engine.predict(
            model=self.model,
            data_path=str(image_path),
            return_predictions=True,
        )

        if not predictions:
            raise RuntimeError("Prediction failed.")

        batch = cast(Any, predictions[0])

        anomaly_map = batch.anomaly_map[0].detach().cpu().numpy()
        score = float(batch.pred_score[0].detach().cpu().item())
        label = bool(batch.pred_label[0].detach().cpu().item())

        anomaly_map_resized = cv2.resize(
            anomaly_map,
            (original_np.shape[1], original_np.shape[0]),
        )

        overlay = create_overlay(
            image_np=original_np,
            anomaly_map=anomaly_map_resized,
        )

        overlay_path = save_overlay_image(
            overlay=overlay,
            output_dir=OUTPUT_DIR,
        )

        return PredictionResult(
            model=self.model_name,
            score=score,
            label=label,
            overlay_path=str(overlay_path),
        )
