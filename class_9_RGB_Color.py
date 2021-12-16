from operator import add
from abc import ABC, abstractmethod


class Color1:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):  # это для конечного пользователя
        return f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}'


class Color2:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r, g, b):
        self.rgb = r, g, b  # один раз создали и больше не создаем через метод

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __str__(self):  # это для конечного пользователя
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}'


class Color3:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, *args):
        if len(args) != 3:
            return None
        self.rgb = tuple(map(self._normalize, args))  # один раз создали и больше не создаем через метод

    def _normalize(self, level):
        return max(min(255, level), 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color3(*map(add, self.rgb, other.rgb)).__str__()
        return False

    def __str__(self):  # это для конечного пользователя
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}'


class Color4:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    symbol = '🟌'

    def __init__(self, *args):
        if len(args) != 3:
            return None
        self.rgb = tuple(map(self._normalize, args))  # один раз создали и больше не создаем через метод

    def _normalize(self, level):
        return max(min(255, level), 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __hash__(self):
        return hash(self.rgb)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color4(*map(add, self.rgb, other.rgb)).__str__()
        return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # это для конечного пользователя через print
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}{self.symbol}{self.END}{self.MOD}'


class Color5:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    symbol = '🟌'

    def __init__(self, *args):
        if len(args) != 3:
            return None
        self.rgb = tuple(map(self._normalize, args))  # один раз создали и больше не создаем через метод

    def _normalize(self, level):
        return max(min(255, level), 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __hash__(self):
        return hash(self.rgb)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color5(*map(add, self.rgb, other.rgb)).__str__()
        return False

    def __mul__(self, c):
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        new_color = tuple(int(F * (i - 128) + 128) for i in self.rgb)
        return Color5(*new_color)

    def __rmul__(self, c):
        return self.__mul__(c)

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # это для конечного пользователя через print
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}{self.symbol}{self.END}{self.MOD}'



class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass


class Color6(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    symbol = '🟌'

    def __init__(self, *args):
        if len(args) != 3:
            return None
        self.rgb = tuple(map(self._normalize, args))  # один раз создали и больше не создаем через метод

    def _normalize(self, level):
        return max(min(255, level), 0)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __hash__(self):
        return hash(self.rgb)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Color6(*map(add, self.rgb, other.rgb)).__str__()
        return False

    def __mul__(self, c):
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        new_color = tuple(int(F * (i - 128) + 128) for i in self.rgb)
        return Color6(*new_color)

    def __rmul__(self, c):
        return self.__mul__(c)

    def __repr__(self):
        return self.__str__()

    def __str__(self):  # это для конечного пользователя через print
        return f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}{self.symbol}{self.END}{self.MOD}'


if __name__ == '__main__':
    print('------Задание 1-------')
    red = Color1(255, 0, 0)
    print(red)

    print('------Задание 2-------')
    print(Color2(255, 0, 0) == Color2(0, 0, 0))
    print(Color2(0, 0, 0) == 3)
    print(3 != Color2(0, 0, 0))
    print(Color2(0, 0, 0) != 3)
    print(Color2(255, 0, 0))

    print('------Задание 3-------')
    red = Color3(255, 0, 0)
    green = Color3(0, 255, 0)
    print(red + green)

    print('------Задание 4-------')
    orange1 = Color4(255, 165, 0)
    red = Color4(255, 0, 0)
    green = Color4(0, 255, 0)
    orange2 = Color4(255, 165, 0)

    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    print('------Задание 5-------')
    red = Color5(255, 0, 0)
    print(0.3 * red)