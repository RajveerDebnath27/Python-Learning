cars=["BMW","Toyota","Range Rover","Audi","Bugatti","Lamborghini"]
bikes=["BMW","Yamaha","Kawasaki","Ducati","Honda"]

# print(len(cars))

def list_size(list_data,n=0):

    if n == len(list_data):
        return None

    if n == len(list_data)-1:
        print(list_data[n])
    
    else:
        print(list_data[n],end=", ")
    return list_size(list_data,n+1)


list_size(cars)
print()
list_size(bikes)

