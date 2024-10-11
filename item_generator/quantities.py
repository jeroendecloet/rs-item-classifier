import re
from enum import Enum

import numpy as np


class DigitEnum(Enum):
    background = 0
    foreground = 1
    shadow = 2


class Quantities:

    @property
    def one(self) -> np.ndarray:
        return np.array([
            [0, 1, 0, 0],
            [1, 1, 2, 0],
            [0, 1, 2, 0],
            [0, 1, 2, 0],
            [0, 1, 2, 0],
            [0, 1, 2, 0],
            [0, 1, 2, 0],
            [1, 1, 1, 0],
            [0, 2, 2, 2],
        ])

    @property
    def two(self) -> np.ndarray:
        return np.array([
        [0, 1, 1, 1, 0, 0],
        [1, 0, 2, 2, 1, 0],
        [0, 2, 0, 0, 1, 2],
        [0, 0, 0, 1, 0, 2],
        [0, 0, 1, 0, 2, 0],
        [0, 1, 0, 2, 0, 0],
        [1, 0, 2, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 2, 2, 2, 2, 2],
    ])

    @property
    def three(self) -> np.ndarray:
        return np.array([
            [0, 1, 1, 0, 0],
            [1, 0, 2, 1, 0],
            [0, 2, 0, 1, 2],
            [0, 1, 1, 0, 2],
            [0, 0, 2, 1, 0],
            [0, 0, 0, 1, 2],
            [1, 0, 0, 1, 2],
            [0, 1, 1, 0, 2],
            [0, 0, 2, 2, 0],
        ])

    @property
    def four(self) -> np.ndarray:
        return np.array([
            [1, 0, 0, 0, 0],
            [1, 2, 0, 0, 0],
            [1, 2, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [1, 2, 1, 2, 0],
            [1, 1, 1, 1, 0],
            [0, 2, 1, 2, 2],
            [0, 0, 1, 2, 0],
            [0, 0, 0, 2, 0],
        ])

    @property
    def five(self) -> np.ndarray:
        return np.array([
            [1, 1, 1, 1, 0],
            [1, 2, 2, 2, 2],
            [1, 2, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 2, 2, 1, 0],
            [0, 0, 0, 1, 2],
            [1, 0, 0, 1, 2],
            [0, 1, 1, 0, 2],
            [0, 0, 2, 2, 0],
        ])

    @property
    def six(self) -> np.ndarray:
        return np.array([
            [0, 0, 1, 1, 0, 0],
            [0, 1, 0, 2, 1, 0],
            [1, 0, 2, 0, 0, 2],
            [1, 2, 1, 1, 0, 0],
            [1, 1, 0, 2, 1, 0],
            [1, 2, 2, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [0, 1, 1, 1, 0, 2],
            [0, 0, 2, 2, 2, 0],
        ])

    @property
    def seven(self) -> np.ndarray:
        return np.array([
            [1, 1, 1, 1, 0],
            [0, 2, 2, 1, 2],
            [0, 0, 1, 0, 2],
            [0, 0, 1, 2, 0],
            [0, 1, 0, 2, 0],
            [0, 1, 2, 0, 0],
            [1, 0, 2, 0, 0],
            [1, 2, 0, 0, 0],
            [0, 2, 0, 0, 0],
        ])

    @property
    def eight(self) -> np.ndarray:
        return np.array([
            [0, 1, 1, 1, 0, 0],
            [1, 0, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [0, 1, 1, 1, 0, 2],
            [1, 0, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [0, 1, 1, 1, 0, 2],
            [0, 0, 2, 2, 2, 0],
        ])

    @property
    def nine(self) -> np.ndarray:
        return np.array([
            [0, 1, 1, 1, 0, 0],
            [1, 0, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [0, 1, 0, 0, 1, 2],
            [0, 0, 1, 1, 1, 2],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 2],
        ])
    @property
    def zero(self) -> np.ndarray:
        return np.array([
            [0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [1, 0, 2, 0, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [0, 1, 0, 1, 0, 2],
            [0, 0, 1, 0, 2, 0],
            [0, 0, 0, 2, 0, 0],
        ])

    @property
    def space(self) -> np.ndarray:
        return np.array([
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
        ])

    @property
    def k(self) -> np.ndarray:
        return np.array([
            [1, 0, 0, 0, 0, 0],
            [1, 2, 0, 1, 0, 0],
            [1, 2, 1, 0, 2, 0],
            [1, 1, 0, 2, 0, 0],
            [1, 1, 2, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [1, 2, 0, 1, 0, 0],
            [1, 2, 0, 0, 1, 0],
            [0, 2, 0, 0, 0, 2],
        ])

    @property
    def m(self) -> np.ndarray:
        return np.array([
            [1, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 1, 2],
            [1, 2, 1, 1, 0, 1, 2],
            [1, 2, 0, 2, 2, 1, 2],
            [1, 2, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 1, 2],
            [0, 2, 0, 0, 0, 0, 2],
        ])

    @property
    def b(self) -> np.ndarray:
        return np.array([
            [1, 1, 1, 1, 0, 0],
            [1, 2, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [1, 1, 1, 1, 0, 2],
            [1, 2, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [1, 1, 1, 1, 0, 2],
            [0, 2, 2, 2, 2, 0],
        ])

    @property
    def q(self) -> np.ndarray:
        return np.array([
            [0, 1, 1, 1, 0, 0],
            [1, 0, 2, 2, 1, 0],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 0, 0, 1, 2],
            [1, 2, 1, 0, 1, 2],
            [1, 2, 0, 1, 0, 2],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 2, 2, 0, 2],
        ])

    @property
    def t(self) -> np.ndarray:
        return np.array([
            [1, 1, 1, 1, 1, 0],
            [0, 2, 1, 2, 2, 2],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 0, 2, 0, 0],
        ])

    def map_digits(self, digit: str) -> np.ndarray:
        digits = {
            "0": self.zero,
            "1": self.one,
            "2": self.two,
            "3": self.three,
            "4": self.four,
            "5": self.five,
            "6": self.six,
            "7": self.seven,
            "8": self.eight,
            "9": self.nine
        }
        return digits[digit]

    @staticmethod
    def suffix_to_multiplier(suffix: str) -> float:
        """ Converts a suffix (k, m, b, q or t) to a multiplier (1e3, 1e6, ...). """
        if (suffix is None) or (suffix == ""):
            return 1
        elif suffix.lower() == "k":
            return 1e3
        elif suffix.lower() == "m":
            return 1e6
        elif suffix.lower() == "b":
            return 1e9
        elif suffix.lower() == "q":
            return 1e12
        elif suffix.lower() == "t":
            return 1e15
        else:
            raise ValueError(f"Unknown suffix `{suffix}`")

    def parse_number(self, number: str | int | float) -> (str, str):
        """
        Parses a number and converts it to a combination of digits and suffix.

        Inputs
        ------
        number: str | int
            Number to parse, e.g. '1234' or '5K'

        Examples
        --------
        >>> self.parse_number("26m")
        ("26", "m")
        >>> self.parse_number("123")
        ("123", "")
        >>> self.parse_number(1234)
        ("1", "k")
        """
        if isinstance(number, str):
            regex = r"(\d+)([kKmMbBtTqQ]?)"
            result = re.search(regex, number)
            if result:
                digits, suffix = result.groups()
                if len(digits) > 3:
                    # Too large numbers that should actually have another suffix, convert it
                    # For example 1000k = 1m
                    multiplier = self.suffix_to_multiplier(suffix)
                    number_ = int(digits) * multiplier
                    digits, suffix = self.parse_number(number_)
            else:
                raise ValueError(f"Could not parse `{number}`!")
        elif isinstance(number, (int, float)):
            # Convert float to int
            number_ = int(number)
            if number_ < 1e5:
                digits = str(number_)
                suffix = ""
            elif 1e5 <= number_ < 1e7:
                digits = str(int(np.floor(number_ / 1e3)))
                suffix = "k"
            elif 1e7 <= number_ < 1e9:
                digits = str(int(np.floor(number_ / 1e6)))
                suffix = "m"
            elif 1e9 <= number_ < 1e12:
                digits = str(int(np.floor(number_ / 1e9)))
                suffix = "b"
            elif 1e12 <= number_ < 1e15:
                digits = str(int(np.floor(number_ / 1e12)))
                suffix = "q"
            elif number_ >= 1e15:
                digits = str(int(np.floor(number_ / 1e15)))
                suffix = "t"
            else:
                raise ValueError(f"Not possible: {number_}")
        else:
            raise ValueError(f"Number should be either `str`, `int` or `float`, not `{type(number)}`!")

        return digits, suffix

    def build_digit_image(self, digits: str, suffix: str):
        numbers = list(str(digits))
        number_arrays = list()
        for n in numbers:
            number_arrays.append(self.map_digits(n))
            if n != "1":
                number_arrays.append(self.space)

        if (suffix is not None) and (suffix != ""):
            number_arrays.append(getattr(self, suffix))
        number_array = np.concatenate(number_arrays, axis=1)

        mask_background = number_array == DigitEnum.background.value
        mask_foreground = number_array == DigitEnum.foreground.value
        mask_shadow = number_array == DigitEnum.shadow.value

        yellow = np.array([1, 1, 0, 1])  # for sub K = 1e0
        white = np.array([1, 1, 1, 1])  # for K = 1e3
        green = np.array([0, 255, 128, 255]) / 255  # for M = 1e6
        blue = np.array([102, 152, 255, 255]) / 255  # for B = 1e9
        purple = np.array([189, 50, 243, 255]) / 255  # for T = 1e12
        orange = np.array([255, 129, 0, 255]) / 255  # for Q = 1e15
        black = np.array([0, 0, 0, 1])

        if (suffix is None) or (suffix == ""):
            color = yellow
        elif suffix.lower() == "k":
            color = white
        elif suffix.lower() == "m":
            color = green
        elif suffix.lower() == "b":
            color = blue
        elif suffix.lower() == "t":
            color = purple
        elif suffix.lower() == "q":
            color = orange
        else:
            raise ValueError(f"Unknown suffix `{suffix}`!")

        color_array = np.ones(number_array.shape[:2] + (4,))
        color_array[mask_background] = np.array([0, 0, 0, 0])  # Set alpha to 0 for transparency
        color_array[mask_foreground] = color
        color_array[mask_shadow] = black
        return color_array

    def __call__(self, number: str | int) -> np.ndarray:
        digits, suffix = self.parse_number(number)
        digit_image = self.build_digit_image(digits, suffix)
        return digit_image


class QuantityGenerator:
    """ Class for generating random digits. """
    rng: np.random.Generator

    def __init__(self, seed: int = 46) -> None:
        self.rng = np.random.default_rng(seed=seed)
        self.letters = list(" kmbqt")
        # TODO: Find better distribution
        # TODO: also include 0
        self.letter_probabilities = np.array([9, 4, 4, 2, 1, 1], dtype=float)
        self.letter_probabilities /= np.sum(self.letter_probabilities)
        self.quantities = Quantities()

    def generate_number(self):
        """ Generates a letter and a corresponding number."""
        # First pick a letter
        letter = self.rng.choice(self.letters, p=self.letter_probabilities)
        if letter == " ":
            max_value = 99999
        elif letter == "k":
            max_value = 9999
        else:
            max_value = 999
        digit = self.rng.integers(max_value)
        return f"{digit}{letter}"

    def __call__(self, number: str | int = None) -> np.ndarray:
        if number is None:
            number = self.generate_number()
        number_image = self.quantities(number)
        return number_image
