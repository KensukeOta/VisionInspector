from anomalib.models.image.padim import Padim

from app.core.config import PADIM_CHECKPOINT
from app.core.model_names import ModelName


class ModelLoader:
    def __init__(self) -> None:
        self._registry: dict[ModelName, Padim] = {}

    def get(self, model_name: ModelName) -> Padim:
        if model_name not in self._registry:
            self._registry[model_name] = self._create(model_name)

        return self._registry[model_name]

    def _create(self, model_name: ModelName) -> Padim:
        creators = {
            "padim": self._load_padim,
        }

        try:
            return creators[model_name]()
        except KeyError as exc:
            raise ValueError(f"Unsupported model: {model_name}") from exc

    def _load_padim(self) -> Padim:
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


model_loader = ModelLoader()
