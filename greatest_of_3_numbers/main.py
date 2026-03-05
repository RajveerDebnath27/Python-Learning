num = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num == num2 and num == num3:
    print("all numbers are equal")
else:
    if num >= num2 and num >= num3:
        print(num, "is greater than ", num2, "and", num3)

    elif num2 >= num and num2 >= num3:
        print(num2, "is greater than ", num, "and", num3)

    elif num3 >= num2 and num3 >= num:
        print(num3, "is greater than ", num2, "and", num)

