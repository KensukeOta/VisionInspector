from pathlib import Path
from typing import cast

import cv2
import numpy as np
import torch
from torch import Tensor
from torchvision import transforms

from app.core.config import OUTPUT_DIR
from app.schemas.prediction_result import PredictionResult
from app.services.model_loader import ModelName, model_loader
from app.utils.image_utils import (
    create_overlay,
    load_rgb_image,
    save_overlay_image,
)


class InferenceService:
    def __init__(self, model_name: ModelName = "padim") -> None:
        self.model_name = model_name
        self.model = model_loader.get(model_name)
        self.transform = transforms.Compose(
            [
                transforms.Resize((256, 256)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225],
                ),
            ]
        )

    def predict(self, image_path: Path) -> PredictionResult:
        image = load_rgb_image(image_path)
        original_np = np.array(image)

        transformed = cast(Tensor, self.transform(image))
        input_tensor = transformed.unsqueeze(0)

        with torch.no_grad():
            prediction = self.model(input_tensor)

        anomaly_map = prediction.anomaly_map.squeeze().detach().cpu().numpy()
        score = float(prediction.pred_score.squeeze().detach().cpu().item())
        label = bool(prediction.pred_label.squeeze().detach().cpu().item())

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
