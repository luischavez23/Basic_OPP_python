from geometric_figure import Geometric
from color import Color

class Square(Geometric, Color):
    
    def __init__(self, measure, color):
        Geometric.__init__(self, measure, measure)
        Color.__init__(self, color)
    
    def __str__(self):
        return f'Square\n{Geometric.__str__(self)}\n{Color.__str__(self)}'
    
    def area(self):
        return f'\nSquare\nArea: {self._length*self._width} cm\n'