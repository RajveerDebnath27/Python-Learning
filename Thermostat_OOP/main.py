# Create a class called Thermostat.
# __init__ takes a current_temperature (integer).
# Create a set_temperature(self, new_temp) method.
# If new_temp is between 15 and 30 (inclusive), update self.current_temperature and
# print "Temperature updated!".
# Otherwise, print an error message and do not change the temperature.

class Thermostat:
    def __init__(self, c_temp):
        self.c_temp = c_temp

    def set_temp(self, new_temp):

        if 15 < new_temp < 30:
            self.c_temp = new_temp
            print("Temperature updated!")


        else:
            print("Error temperature cannot be changed!")



T1 = Thermostat(25)
T2 = Thermostat(35)
T3 = Thermostat(45)
print(T1.c_temp)
print(T2.c_temp)
print(T3.c_temp)
print(T1.set_temp(17))
print(T2.set_temp(15))
print(T3.set_temp(28))