f=open("practice.txt","r")
data=f.read()
new_data = data.replace("java","python")
f.close()
print("\n \n \n")
f=open("practice.txt","w")

f.write(new_data)

f.close()

f=open("practice.txt","r")
print(f.read())
f.close()