from car import Car
from boat import Boat

class AmphibiousCar(Car, Boat):
    def __init__(self,model,wheels,propellers):
        super().__init__(wheels=wheels, propellers=propellers)
        self.model = model
        # print("AmphibiousCar class called")

