class Arithmetic:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def addition(self):
        return self.number1 + self.number2
    
    def subtraction(self):
        return self.number1 - self.number2
    
    def multiplication(self):
        return self.number1 * self.number2 
    
    def division(self):
        return self.number1//self.number2

arithmetic1 = Arithmetic(10,5)
print(f"Addition: {arithmetic1.addition()}")
print(f"Subtraction: {arithmetic1.subtraction()}")
print(f"Multiplication: {arithmetic1.multiplication()}")
print(f"Division: {arithmetic1.division()}")