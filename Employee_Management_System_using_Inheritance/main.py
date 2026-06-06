# 1. The Parent Class: Employee
# __init__ should take a name and a salary.
# Create a method called work(self) that prints: "[name] is working."
# 2. The Child Class: Developer
# Make it inherit from Employee.
# Give it a unique method called code(self) that prints: "[name] is writing Python code!"
# 3. Destructor Integration:
# Add the __del__(self) method inside the parent Employee class so that whenever any employee
# (or developer) is deleted, it prints: "Goodbye [name]! Access revoked."
# Your Test Script Goal:
# Create a Developer object named "Apurba" with a salary of 120000.
# Make him call his inherited work() method.
# Make him call his unique code() method.
# Use the del keyword to delete him, and watch your destructor trigger its goodbye message!

from developer import Developer

d1 = Developer("Apurba", 120000)
d1.work()
d1.code()

print("--- Print Manual cleanup now ---")
del d1
print("--- Script has officially finished ---")