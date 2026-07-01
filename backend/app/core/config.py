from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

CHECKPOINT_DIR = BASE_DIR / "checkpoints"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

PADIM_CHECKPOINT = CHECKPOINT_DIR / "padim_bottle.ckpt"
