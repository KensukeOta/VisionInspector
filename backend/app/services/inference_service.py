from pathlib import Path

import cv2
import numpy as np
import torch
from torchvision import transforms

from app.core.config import OUTPUT_DIR
from app.services.model_loader import load_padim_model
from app.utils.image_utils import (
    create_overlay,
    load_rgb_image,
    save_overlay_image,
)


class InferenceService:
    def __init__(self) -> None:
        self.model = load_padim_model()
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

    def predict(self, image_path: Path) -> dict:
        image = load_rgb_image(image_path)
        original_np = np.array(image)

        input_tensor = self.transform(image).unsqueeze(0)

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

        return {
            "score": score,
            "label": label,
            "overlay_path": str(overlay_path),
        }
