tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=int(input("Enter a number among 1, 4, 9, 16, 25, 36, 49, 64, 81, 100: "))


n=0
while n<len(tpl):
    var = tpl[n]
    n+=1
    if var==x:
        print(var,"Found at index",n)
        break
    if n==len(tpl):
        print("Entered Wrong Number")

