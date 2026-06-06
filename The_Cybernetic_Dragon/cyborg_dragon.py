from beast import Beast
from robot import Robot

class CyborgDragon(Robot,Beast):
    def __init__(self,name, battery_capacity, fang_length):
        self.name = name
        super().__init__(battery_capacity=battery_capacity, fang_length=fang_length)


    def laser_breath(self):
        print(f"{self.name} fires a plasma laser")

    def __del__(self):
        print(f"{self.name} has powered down and decomposed")