class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area_rectangle(self):
        return self.length * self.width
    

rectangle1 = Rectangle(4,10)
print(f"Area of rectangle: {rectangle1.area_rectangle()}")
        