n=int(input("Enter the factorial Number: "))

x=1

for i in range(1,n+1,1):
    x*=i

print("The factorial of",n,"is",x)