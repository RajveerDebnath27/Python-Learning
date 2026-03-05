number = int(input("Enter a number: "))

def oddEven(num):
    if num % 2 == 0 and num != 0 :
        print("Even")
    elif num == 0 :
        print("Zero")
    else:
        print("Odd")

    return num

oddEven(number)