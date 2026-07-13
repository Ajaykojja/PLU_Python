marks = [45, 57, 78, 58, 39, 78]

n = len(marks)

for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Marks in ascending order:")
print(*marks)

