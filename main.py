class Car:
    def __init__(self, make: str, model: str, year: int, price: int):
        if not isinstance(make, str):
            raise TypeError(f"make must be a string, got {type(make).__name__} instead")
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - ${self.price}")

class Dealership:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def display_inventory(self):
        print("Dealership Inventory:")
        for car in self.cars:
            car.display_info()

# Creating some car instances
car1 = Car("Toyota", "Corolla", 2020, 20000)
car2 = Car("Honda", "Civic", 2022, 22000)
car3=Car("Jeep","Grand Cherokee","2024","75000")

# Creating a dealership instance
dealership = Dealership()

# Adding cars to the dealership
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)

# Displaying the dealership inventory
dealership.display_inventory()