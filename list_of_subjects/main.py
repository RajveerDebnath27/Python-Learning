subject=["python","java","C++","python","javascript","java","python","java","C++","C"]
#Now the problem is one classroom is needed for one subject.So how many classroom are needed by
#all the students.

subjectSet = set(subject)   #store the list in a set so that the multiple numbers of same subject became one
print(subjectSet)
print(len(subjectSet),"classroom are needed")