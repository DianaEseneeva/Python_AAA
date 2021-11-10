import keyword
import json


class NewObj:
    """
    Creates python objects that can be referred with the dot
    """

    def __init__(self, dict_params):
        for key, value in dict_params.items():
            if keyword.iskeyword(key):
                key = key + '_'
            if isinstance(value, dict):
                value = NewObj(value)
            setattr(self, key, value)

        if 'price' not in self.__dict__.keys():
            setattr(self, 'price', 0)

        if self.price < 0:
            raise ValueError('price must be >= 0')


class ColorizeMixin:
    """
    Changes the color of __repr__ output
    """
    repr_color_code = 33  # yellow

    def __repr__(self):
        for_color = '\033[5;' + str(self.repr_color_code) + ';10m'
        info = str(self.title) + '|' + str(self.price) + '₽'
        return for_color + info


class BaseAdvert:

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(NewObj, ColorizeMixin, BaseAdvert):
    """
    Creates advert-object from json-file
    """
    def __init__(self, params):
        super().__init__(params)


if __name__ == '__main__':
    corgi = """{"title": "Вельш-корги",
                "price": 1000,
                "class": "dogs",
                "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                            }
                }"""
    corgi = json.loads(corgi)
    corgi_dog = Advert(corgi)
    print(corgi_dog)

