# File 1: robot.py (Parent 1)
# Create a class Robot.
# Its __init__ should take battery_capacity and kwargs.
# Remember to call super().__init__(kwargs).
# It has a method charge(self) that prints: "Charging system to [battery_capacity]mAh."
# File 2: beast.py (Parent 2)
# Create a class Beast.
# Its __init__ should take fang_length and kwargs. Remember to call super().__init__(kwargs).
# It has a method roar(self) that prints: "Roaring with [fang_length]cm fangs!"
# File 3: cyborg_dragon.py (The Child Class)
# Create a class CyborgDragon that inherits from both Robot and Beast.
# Its __init__ should take name, battery_capacity, and fang_length.
# Use super().__init__(...) to forward the correct keyword arguments to the parents,
# and save self.name = name.
# Create a unique method laser_breath(self) that prints: "[name] fires a plasma laser!"
# Destructor: Add a __del__(self) method here that prints: "[name] has powered down
# and decomposed."
# File 4: main.py (Execution)
# Import CyborgDragon.
# Create your monster: dragon = CyborgDragon("MechaDraco", 10000, 15).
# Call .charge(), .roar(), and .laser_breath().
# Explicitly delete your dragon using the del keyword
# to trigger the destructor immediately before the script ends.

from cyborg_dragon import CyborgDragon

dragon = CyborgDragon("MechaDragon",10000,15)
dragon.roar()
dragon.charge()
dragon.laser_breath()

print()
print("print manual cleanup")
del dragon
print("Script is finished")