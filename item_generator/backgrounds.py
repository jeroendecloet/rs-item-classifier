import numpy as np

from utils import data_utils as du
from utils import image_utils as iu


class BaseBackground:
    """ Base class for background generation. Contains generic functions. """
    rng: np.random.Generator

    def __init__(self, seed: int = 46) -> None:
        self.rng = np.random.default_rng(seed=seed)

        self.image_ids = None
        self.n_images = None
        self.remaining_indices = None

    def sample_image(self, **kwargs) -> str:
        """ Selects the image ID to generate the background from. """
        if self.n_images == 1:
            # Shortcut for a single image
            yield self.image_ids[0]

        while True:
            # Generate newly shuffled
            if (self.remaining_indices is None) or len(self.remaining_indices) == 0:
                self.remaining_indices = self.rng.choice(self.n_images, size=self.n_images, replace=False, shuffle=True, **kwargs)

            # Pop the first index
            index = self.remaining_indices[0]
            self.remaining_indices = self.remaining_indices[1:]
            yield self.image_ids[index]

    def sample_patch(self, image: np.ndarray, size: tuple[int, int]) -> np.ndarray:
        """ Samples a patch from the selected image. """
        h, w = image.shape[-2:]
        h_selected = self.rng.integers(low=0, high=h - size[0])
        w_selected = self.rng.integers(low=0, high=w - size[1])
        return image[..., h_selected:h_selected + size[0], w_selected:w_selected + size[1]]

    def __call__(self, size: tuple[int, int]) -> np.ndarray:
        image_filename = next(iter(self.sample_image()))
        image = iu.load_png(image_filename)
        image = iu.convert_dimensions(image, "chw")
        patch = self.sample_patch(image, size=size)
        return patch


class BankBackground(BaseBackground):
    """ Generates a background from the bank. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.directory = du.get_dataset_path() / "backgrounds"
        self.image_ids = list(self.directory.glob("*.png"))
        self.n_images = len(self.image_ids)


class InventoryBackground(BaseBackground):
    """ Generates a background from the inventory. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.directory = du.get_dataset_path() / "inventory"
        self.image_ids = list(self.directory.glob("*.png"))
        self.n_images = len(self.image_ids)

class RunescapeBackground(BaseBackground):
    """ Generates a background from a Runescape image. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.directory = du.get_dataset_path() / "runescape"
        self.image_ids = list(self.directory.glob("*.png"))
        self.n_images = len(self.image_ids)


class TransparentBackground(BaseBackground):
    """ Generates a background from the mix of two other backgrounds. """
    pass
