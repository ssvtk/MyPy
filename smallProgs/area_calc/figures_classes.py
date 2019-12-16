import math


class Circle:

    def __init__(self, params):
        self.r = float(params[0])

    def area(self):
        return round(math.pi * (self.r ** 2), 3)

    def __str__(self):
        return f'Circle with r = {self.r} and S = [{self.area()}]'


class Triangle:

    def __init__(self, params):
        self.side1, self.side2, self.side3 = float(params[0]), float(params[1]), float(params[2])

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt((p * (p - self.side1) * (p - self.side2) * (p - self.side3))), 3)

    def __str__(self):
        return f'Triangle with a = {self.side1}, b = {self.side2}, c = {self.side3} and S = [{self.area()}]'


class Rect:

    def __init__(self, params):
        self.side1, self.side2 = float(params[0]), float(params[1])

    def area(self):
        return round(self.side1 * self.side2, 3)

    def __str__(self):
        return f'Rect with a = {self.side1}, b = {self.side2} and S = [{self.area()}]'
