# Basic Car class
class Car:
    def __init__(self, make, model, year, color):
        # attributes of the Car
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.__mileage = 0   # (encapsulation)
    
    def drive(self, distance):
        self.__mileage += distance
        print(f"Driving {distance} miles in your {self.color} {self.make} {self.model}")
    
    def get_info(self):
        return f"{self.year} {self.color} {self.make} {self.model}"
    
    def get_mileage(self):
        return self.__mileage


# ElectricCar inherits from Car (inheritance)
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        # Call the parent class constructor
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity
    
    # Override the parent class method (polymorphism)
    def get_info(self):
        return f"{self.year} {self.color} {self.make} {self.model} - Electric ({self.battery_capacity} kWh)"
    
    def charge(self):
        print(f"Charging the {self.make} {self.model}...")



my_car = Car("Toyota", "Corolla", 2023, "Blue")
print(my_car.get_info())
my_car.drive(100)
print(f"Current mileage: {my_car.get_mileage()} miles")

my_electric_car = ElectricCar("Tesla", "Model 3", 2024, "Red", 75)
print(my_electric_car.get_info())
my_electric_car.drive(150)
my_electric_car.charge()
print(f"Current mileage: {my_electric_car.get_mileage()} miles")