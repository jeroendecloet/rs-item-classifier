from pathlib import Path

from utils import image_utils as iu
from utils import data_utils as du


class Items:

    def __init__(self):
        self.item_folder = du.get_dataset_path() / "item_inventory_images"

        self.item_paths = None
        self.item_names = None

        self.discover_items()

    def discover_items(self):
        """ Find all items in the item_folder. """
        self.item_paths = dict()
        # Collect all image file paths
        for path in Path(self.item_folder).rglob('*'):
            if path.is_file() and path.suffix.lower() in [".png"]:
                self.item_paths[path.stem] = path
        print(f"Total images found: {len(self.item_paths)}")

        self.item_names = list(self.item_paths.keys())

    def generate_random_item_name(self) -> str:
        """ Picks a random item and returns its name. """
        pass

    def __call__(self, item_name: str = None, item_id: int = None):
        """ Loads a certain item. """
        if item_name is not None:
            pass
        elif item_id is not None:
            item_name = self.item_names[item_id]
        else:
            item_name = self.generate_random_item_name()

        item_path = self.item_paths[item_name]
        item = iu.load_png(item_path)
        return item

