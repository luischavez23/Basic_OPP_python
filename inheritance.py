class Vehicle:
    
    def __init__(self, color, wheel):
        self.color = color
        self.wheel = wheel
    
    def __str__(self):
        return f'Color: {self.color}\nWheel: {self.wheel}'

class Car(Vehicle):
    
    def __init__(self, color, wheel, speed):
        super().__init__(color, wheel)
        self.speed = speed
    
    def __str__(self):
        return f'Car\n{super().__str__()}\n{self.speed} km/h\n'

class Bike(Vehicle):
    
    def __init__(self, color, wheel, type_bike):
        super().__init__(color, wheel)
        self.type_bike = type_bike
    
    def __str__(self):
        return f'Bike\n{super().__str__()}\nType: {self.type_bike}\n'

car1 = Car('Green', 4, 10000)
bike1 = Bike('Red', 2, 'Mountain Bike')
print(car1)
print(bike1)