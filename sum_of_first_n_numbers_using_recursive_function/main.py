def calc_sum(n):

    if n<1:
       return 0

    return n+calc_sum(n - 1)


i= int(input("Enter a number: "))

print("The sum of 1st n numbers using recursive function is: ",end=" ")
print(calc_sum(i))
