# This method is responsible for creating a new instance of a class. It allocates memory and returns the new object. It is called before __init__.


class ClassName:
    def __new__(cls, parameters):
        instance = super(ClassName, cls).__new__(cls)
        return instance
    
# This method initializes the newly created instance and is commonly used as a constructor in Python. It is called immediately after the object is created by __new__ method and is responsible for initializing attributes of the instance.

class ClassName:
    def __init__(self, parameters):
        self.attribute = value
        
        
# default constructor 
class Car:
    def __init__(self):

        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)

# parameterized construtor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)