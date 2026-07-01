from functools import lru_cache

from anomalib.models.image.padim import Padim

from app.core.config import PADIM_CHECKPOINT


@lru_cache(maxsize=1)
def load_padim_model() -> Padim:
    if not PADIM_CHECKPOINT.exists():
        raise FileNotFoundError(f"Checkpoint not found: {PADIM_CHECKPOINT}")

    model = Padim.load_from_checkpoint(
        checkpoint_path=str(PADIM_CHECKPOINT),
        backbone="resnet18",
        layers=["layer1", "layer2", "layer3"],
        pre_trained=True,
    )

    model.eval()
    return model
