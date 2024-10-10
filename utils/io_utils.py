import json
from pathlib import Path
from typing import Any


def load_json(filename: Path) -> Any:
    """ Loads a JSON file. """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data


def save_json(data: Any, filename: Path) -> None:
    """ Saves a JSON file. """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)
