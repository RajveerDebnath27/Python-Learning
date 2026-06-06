# File 1: car.py (Parent 1)
# Create a class Car.
# Its __init__ should accept wheels and kwargs. It must call super().__init__(kwargs).
# It has a method drive(self) that prints: "Driving on land with [wheels] wheels."
# File 2: boat.py (Parent 2)
# Create a class Boat.
# Its __init__ should accept propellers and kwargs. It must call super().__init__(kwargs).
# It has a method swim(self) that prints: "Swimming in water using [propellers] propellers."
# File 3: amphibious_car.py (The Child)
# Create a class AmphibiousCar that inherits from both Car and Boat.
# Its __init__ should accept model, wheels, and propellers.
# It should use super().__init__(wheels=wheels, propellers=propellers)
# to trigger both parents.
# File 4: main.py (Execution)
# Import AmphibiousCar.
# Create an object: vehicle = AmphibiousCar("PythonAmphibian", 4, 2).
# Call .drive() and .swim().

from amphibious import AmphibiousCar

Vehicle = AmphibiousCar("pythonAmphibian",4,2)

Vehicle.drive()
Vehicle.swim()