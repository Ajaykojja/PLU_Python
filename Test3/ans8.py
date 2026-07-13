priority = [2, 5, 1, 4, 3]

print("Original Priority List:")
print(priority)

n = len(priority)

for i in range(n):
    for j in range(0, n - i - 1):
        if priority[j] < priority[j + 1]:
            temp = priority[j]
            priority[j] = priority[j + 1]
            priority[j + 1] = temp

print("Emergency Queue:")
print(priority)