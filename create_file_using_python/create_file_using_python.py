f=open("practice.txt","w")

f.write("Hi everyone!\n we are learning File I/0 \n using java. \n I like programming java")

f.close()

f=open("practice.txt","r")
print(f.read())
f.close()


