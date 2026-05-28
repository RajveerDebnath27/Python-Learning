# Create a class called Smartphone.
# The Constructor: It should take a brand name (string) and a starting battery_level (integer, e.g., 50).
# Method 1: use_phone(time_used)
# This should subtract time_used * 2 from the battery_level (simulating the battery draining over time).
# Constraint: If the battery drops below 0, just set self.battery_level = 0 and print "Phone died!".
# Method 2: charge_phone(amount)
# This should add the amount to the battery_level.
# Constraint: If the battery goes over 100, overwrite it back to exactly 100 (because a battery can't hold 105%) and
# print "Fully Charged!".
# This one requires you to add/subtract in some places, and strictly overwrite in others based on your if/else checks!


class Smartphone:
    def __init__(self, brand,battery_level):
        self.brand = brand
        self.battery_level = battery_level

    def use_phone(self, time_used):
        self.battery_level -= time_used * 2
        if self.battery_level <= 0:
            self.battery_level = 0
            print("Phone died!")
        return self.battery_level

    def charge_phone(self, ammount):
        self.battery_level += ammount
        if self.battery_level >= 100:
            self.battery_level = 100
            print("Phone charged!")
        return self.battery_level




s1=Smartphone("Samsung", 86)
# print(s1.brand, s1.battery_level)
print(f"Initailizing {s1.brand} - {s1.battery_level}")
# s1.use_phone(2)
print(f"Battery after use: {s1.use_phone(2)}")
# print(s1.charge_phone(20))
print(f"Battery after charge: {s1.charge_phone(20)}")
