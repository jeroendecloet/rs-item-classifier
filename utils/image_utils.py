from PIL import Image

import numpy as np


def load_png(filename) -> np.ndarray:
    """ Loads a PNG image and returns it as numpy array with format (H, W, C). """
    image = Image.open(filename)
    image_rgba = image.convert("RGBA")
    return np.array(image_rgba)


def identify_shape(shape: tuple) -> str:
    """
    Identifies the height, width and/or channel of the shape of an image.
    """
    if len(shape) < 2:
        raise NotImplementedError("Identifying shapes with less than two dimensions is not supported!")
    elif len(shape) == 2:
        # Assume (H, W)
        return "hw"
    elif len(shape) == 3:
        # Assume the channel with the smallest size is the channel dimension
        channels = np.argmin(shape)
        dimensions = ["h", "w"]
        dimensions.insert(channels, "c")
        return "".join(dimensions)
    elif len(shape) == 4:
        # Assume batch is first
        return "b" + identify_shape(shape[1:])
    else:
        raise NotImplementedError("Identifying shapes with more than four dimension is not supported!")


def identify_dimensions(image: np.ndarray) -> str:
    """ Identifies the height, width and/or channel dimensions for an image. """
    return identify_shape(image.shape)

def convert_dimensions(image: np.ndarray, target: str, source: str = None) -> np.ndarray:
    """
    Extends/reduces the dimensions of an image with certain shape.
    Can convert shapes (H, W) <--> (C, H, W) <--> (H, W, C).
    """
    if source is None:
        source = identify_dimensions(image)

    # Image already has the right dimensions
    if source == target:
        return image

    shape = image.shape
    if len(target) == 2:
        channel_index = source.index("c")
        if shape[channel_index] == 1:
            return np.squeeze(image, channel_index)
        else:
            raise ValueError(f"Dimensions cannot be reduced! Image shape `{shape}`, source `{source}`, target `{target}`")
    elif len(target) == 3:
        if len(source) < len(target):
            # (H, W) -> (H, W, C) / (C, H, W)
            channel_index = target.index("c")
            return np.expand_dims(image, channel_index)
        elif len(source) == len(target):
            # (H, W, C) <--> (C, H, W)
            moves = [target.index(i) for i in source]
            return np.moveaxis(image, list(range(len(source))), moves)
        elif len(source) > len(target):
            raise NotImplementedError("Reducing the shape with more than four dimensions is not supported yet!")
    else:
        raise NotImplementedError("Extending the shape to four dimensions or more is not supported yet!")

