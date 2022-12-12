from math import pi


class Circle:
    def __init__(self, r):
        self._r = r

    def area(self):
        return pi * (self._r ** 2)


main_circle = Circle(2)
print(main_circle.area())
