from geometric_figure import *
from color import *

class Square(Geometric, Color):
    
    def __init__(self, length, width, color):
        Geometric.__init__(self, length, width)
        Color.__init__(self, color)
    
    def area(self):
        return f'\nSquare\nArea: {self._length*self._width} cm\nColor: {self._color}'

side = int(input('Measure square: '))
color_square = input('Color square: ')
square1 = Square(side, side, color_square)
print(square1.area())

