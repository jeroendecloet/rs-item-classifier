import numpy as np

import item_generator.backgrounds as bgs
import item_generator.items as itm
import item_generator.quantities as qnt


ITEM_SHAPE = (32, 36)  # (H, W)


class SingleItemGenerator:
    def __init__(self):
        self.background_generator = bgs.BankBackground()
        self.item_generator = itm.Items()
        self.quantity_generator = qnt.QuantityGenerator()

    def combine(self, image1, image2):
        image = image1
        image2_shape = image2.shape

        # TODO: fix for image2.shape > image1.shape
        image_patch = image[:image2_shape[0], :image2_shape[1], :]
        image_patch[image2[..., 3] > 0] = image2[image2[..., 3] > 0]
        return image

    def combine_all(self, background: np.ndarray, item: np.ndarray, quantity: np.ndarray) -> np.ndarray:
        print("background.shape", background.shape)
        print("item.shape", item.shape)
        print("quantity.shape", quantity.shape)
        image = self.combine(background, item)
        image = self.combine(image, quantity)
        return image

    def generate(self):
        background = self.background_generator(ITEM_SHAPE)
        item = self.item_generator(item_id=1000)
        quantity = self.quantity_generator()

        image = self.combine_all(background, item, quantity)
        return image