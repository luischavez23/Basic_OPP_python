class Geometric:
    
    def __init__(self, width, length):
        self._width = width
        self._length = length

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        self._length = length
    
    def __str__(self):
        return f'Width: {self._width}\nLength: {self._length}'





