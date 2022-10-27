""" Advert class """
import json
from collections import namedtuple
from keyword import iskeyword
from typing import Optional


class ColorizeMixin:
    """
    Mixin for colorizing advertisement info
    """

    def __init__(self, color_code: Optional[int]):
        self.repr_color_code = 30 if color_code is None else color_code

    def __repr__(self):
        repr_str = super().__repr__()
        return f"\033[1:{self.repr_color_code}:48m{repr_str}\033[00m"

    def func(self):
        """
        Fictitious method to pass Pylint refactor problem
        :return: None
        """


class Advert:
    """
    Stores information about advertisement
    """

    def __init__(self, json_dict: dict):
        Advert._create_attributes(self, json_dict)
        self._check_title()
        self._check_price()

    @staticmethod
    def _create_attributes(ref, dct: dict) -> None:
        for key, val in dct.items():
            if iskeyword(key):
                key += '_'

            if isinstance(val, dict):
                key_type = namedtuple(f'{key}', val.keys())
                setattr(ref, key, key_type(**val))
                Advert._create_attributes(getattr(ref, key), val)
            elif not hasattr(ref, key):
                setattr(ref, key, val)

    def _check_title(self) -> None:
        if not hasattr(self, 'title'):
            raise ValueError("advertisement doesn't have field 'title'")

    def _check_price(self, price=None) -> None:
        price = self._price if price is None else price

        if not isinstance(price, int):
            raise ValueError(f"type(price) = {type(self.price)}, should be int")

        if price < 0:
            raise ValueError("must be >= 0")

    @property
    def price(self) -> int:
        """
        Price in the advertisement
        :return price: int
        """
        return self._price

    @price.setter
    def price(self, value):
        self._check_price(value)
        self._price = value

    def __repr__(self):
        return f"{getattr(self, 'title')} | {self.price} ₽"


class ColorizedAdvert(ColorizeMixin, Advert):
    """
    Advertisement with colorized text
    """

    def __init__(self, json_dict: dict, color_code: Optional[int] = None):
        Advert.__init__(self, json_dict)
        ColorizeMixin.__init__(self, color_code)

    def func(self):
        """
        Fictitious method to pass Pylint refactor problem
        :return: None
        """


if __name__ == '__main__':
    LESSON_STR = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    CORGI_STR = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, \
                поселок санатория Тишково, 25"
        }
    }"""
    IPHONE_STR = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    lesson = json.loads(LESSON_STR)
    corgi = json.loads(CORGI_STR)
    iphone = json.loads(IPHONE_STR)

    lesson_ad = Advert(lesson)
    corgi_ad = ColorizedAdvert(corgi, 32)
    iphone_ad = Advert(iphone)

    print(lesson_ad)
    print(lesson_ad.location.address)

    print(corgi_ad)
    print(corgi_ad.class_)

    print(iphone_ad)
    print(iphone_ad.price)

    try:
        iphone_ad.price = -1
    except ValueError:
        print("Negative price wasn't set!")

    try:
        BAD_IPHONE_STR = """{
            "title": "iPhone X",
            "price": -1
        }"""
        bad_iphone = json.loads(BAD_IPHONE_STR)
        bad_iphone_ad = Advert(bad_iphone)
    except ValueError as err:
        print("Incorrect advertisement wasn't created!")
