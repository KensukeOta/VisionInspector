import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

CHECKPOINT_DIR = BASE_DIR / "checkpoints"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

PADIM_CHECKPOINT = CHECKPOINT_DIR / "padim_bottle.ckpt"


def get_allow_origins() -> list[str]:
    raw_origins = os.getenv("ALLOW_ORIGINS")

    if not raw_origins:
        return ["http://localhost:5173"]

    return [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
