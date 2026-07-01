from pathlib import Path
from typing import cast
from uuid import uuid4

import cv2
import numpy as np
from PIL import Image


def load_rgb_image(image_path: Path) -> Image.Image:
    return Image.open(image_path).convert("RGB")


def normalize_map(x: np.ndarray) -> np.ndarray:
    return (x - x.min()) / (x.max() - x.min() + 1e-8)


def create_overlay(
    image_np: np.ndarray,
    anomaly_map: np.ndarray,
    alpha: float = 0.45,
) -> np.ndarray:
    anomaly_map = normalize_map(anomaly_map)

    heatmap_input = cast(
        np.ndarray,
        (anomaly_map * 255).astype(np.uint8),
    )

    heatmap = cv2.applyColorMap(
        heatmap_input,
        cv2.COLORMAP_JET,
    )
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    image_float = image_np.astype(np.float32) / 255.0
    heatmap_float = heatmap.astype(np.float32) / 255.0

    overlay = (1 - alpha) * image_float + alpha * heatmap_float
    overlay = np.clip(overlay * 255, 0, 255).astype(np.uint8)

    return overlay


def save_overlay_image(
    overlay: np.ndarray,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{uuid4().hex}.png"
    output_path = output_dir / filename

    Image.fromarray(overlay).save(output_path)

    return output_path
