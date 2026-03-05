myList=[]

list_size=int(input("Enter the size of list :"))
for i in range(list_size):                 #Used for loop to get the list size from user
    p=input(f"Enter value {i+1}: ")
    myList.append(p)

copyList=list.copy(myList)
copyList.reverse()

if myList==copyList:
    print("This list is a Palindrome")

else:
    print("This list is not a Palindrome")