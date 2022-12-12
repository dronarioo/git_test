class Rectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def area(self):
        return self._a * self._b


main_rect = Rectangle(5, 4)
print(main_rect.area())
