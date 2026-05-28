# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Student:
    def __init__(self, name , marks_list):
        self.name = name
        self.marks = marks_list


    def avg(self):
        return sum(self.marks)/len(self.marks)


iname=input("Enter Student Name: ")
# imarks=int(input("Enter Marks 1: "))
# imarks2 = int(input("Enter Marks 2: "))
# imarks3 = int(input("Enter Marks 3: "))


collected_marks = []
for i in range(1,4):
    score= int(input(f"Enter Marks {i}:" ))
    collected_marks.append(score)

s1=Student(iname,collected_marks )
print(s1.name,collected_marks)

# print(s1.name,s1.marks,s1.marks2,s1.marks3)
print(f"The Average of the 3 subjects number is:  {s1.avg()}")
