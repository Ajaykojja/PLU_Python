roll = [67, 78, 98, 56, 59, 35]

num = int(input("Enter roll number: "))

for i in range(len(roll)):
    if roll[i] == num:
        print("Student Found at position", i + 1)
        break
else:
    print("Student Not Found")