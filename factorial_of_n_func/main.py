n=int(input("Enter the of factorial :"))
print(f"calculating {n}!")

def fact(num):
    f=1
    for i in range(1,num+1):
        f = f * i

    print(f)
    return f


fact(n)
