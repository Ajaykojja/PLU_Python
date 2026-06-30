fileobj =open("Student.txt",'w')
fileobj.write("My name is siddarth")
fileobj.close()

fileobj =open("Student.txt",'r')
print(fileobj.read())
fileobj.close()