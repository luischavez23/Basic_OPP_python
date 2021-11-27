class Cube:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
    
    def volume_cube(self):
        return self.width * self.length * self.height
    

width = int(input('Width: '))
length = int(input('Length: '))
height = int(input('Height: '))

cube1 = Cube(width, length, height)
print(f"Volume of Cube: {cube1.volume_cube()} m3")