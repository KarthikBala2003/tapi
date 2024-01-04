# car_imp.py
from car_class import Car

class CarManager:
    def __init__(self):
        self.car_fleet = []

    def add_car_to_fleet(self, make, model, year):
        new_car = Car(make, model, year)
        self.car_fleet.append(new_car)
        print(f"Added {new_car.get_description()} to the fleet.")

    def show_fleet(self):
        print("Car Fleet:")
        for car in self.car_fleet:
            print(car.get_description())

    # Implementing the Car class
    # my_car = Car("Toyota", "Corolla", 2020)

    # print(my_car.get_description())  # Output: 2020 Toyota Corolla

    # print(my_car.read_odometer())   # Output: This car has 0 miles on it.

    # my_car.update_odometer(1500)
    # print(my_car.read_odometer())   # Output: This car has 1500 miles on it.

    # my_car.increase_odometer(300)
    # print(my_car.read_odometer())   # Output: This car has 1800 miles on it.
