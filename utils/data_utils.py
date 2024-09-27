from pathlib import Path

def get_dataset_path() -> Path:
    """ Returns the path to the main data directory. """
    return Path(__file__).parent.parent / "data"
