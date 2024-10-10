from pathlib import Path

from utils import io_utils as io
from utils import image_utils as iu
from utils import data_utils as du


ITEM_FILTER_FILENAME = "item_filter.json"


class Items:

    def __init__(self):
        self.item_folder = du.get_dataset_path() / "item_inventory_images"

        self.item_paths = None
        self.item_names = None
        self.item_filter = None

        self.discover_items()
        self.filter_items()

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

    def load_item_filter(self):
        """ Loads the item filter from JSON. """
        item_filter_path = Path(__file__).parent / ITEM_FILTER_FILENAME
        self.item_filter = io.load_json(item_filter_path)

    def filter_items(self):
        """ Filters the list of items"""
        if self.item_filter is None:
            self.load_item_filter()

        # Loop over item filters
        for filter_name, item_list in self.item_filter.items():
            if filter_name == "remove":
                for item_ in item_list:
                    self.item_names.remove(item_)
            else:
                raise NotImplementedError(f"Filtering for `{filter_name}` is not implemented yet!")

        print(f"Total images after filtering: {len(self.item_names)}")

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

