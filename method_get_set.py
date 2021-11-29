class Person:
    def __init__ (self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    @property
    def name_person(self):
        return f"{self._first_name} {self._last_name}"
    
    @name_person.setter
    def name_person(self, first_name):
        self._first_name = first_name

    
person1 = Person('Luis', 'Chavez', 31)
print(person1.name_person)
person1.name_person = "Pablo"
print(person1.name_person)