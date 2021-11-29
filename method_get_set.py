class Person:
    def __init__ (self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name 
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return self._age 
    
    @age.setter
    def age(self, age):
        self._age = age

    def show_name(self):
        print(f"Name: {self.first_name} {self.last_name}\nAge: {self.age} years old.")

person1 = Person('Luis', 'Chavez', 31)
person1.show_name()
person1.first_name = "Pablo"
person1.age = 32
person1.show_name()