import random
from abc import ABC, abstractmethod


class EmojiMixin:
    emogi = {'grass': '🌿',
             'fire': '🔥',
             'water': '🌊',
             'electric': '⚡'}

    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emogi[self.poketype])


class AnimeMon:

    def __init__(self, exp: float = 0):
        self.__exp = exp

    @property
    @abstractmethod
    def exp(self):
        pass

    @exp.setter
    @abstractmethod
    def exp(self, value):
        pass

    @abstractmethod
    def inc_exp(self, value: int):
        pass


class Pokemon(EmojiMixin, AnimeMon):
    def __init__(self, name: str, poketype: str, exp: float = 0):
        super().__init__()
        self.name = name
        self.poketype = poketype
        self.exp = exp

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value):
        self.__exp = value

    def __str__(self):
        return f'{self.name}/{self.poketype}'

    def inc_exp(self, value: int):
        self.exp += value


class Digimon(AnimeMon):
    def __init__(self, name: str, exp: float = 0):
        super().__init__()
        self.name = name
        self.exp = exp

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value):
        self.__exp = value

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(pokemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ =='__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)

    agumon = Digimon(name='Agumon')
    train(agumon)

    print(agumon.exp)
    print(bulbasaur.exp)