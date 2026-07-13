time = [12.5, 14.5, 16.8, 16.6, 15.8]
n = len(time)

for i in range(n):
    for j in range(n - i - 1):
        if time[j] < time[j + 1]:
            time[j], time[j + 1] = time[j + 1], time[j]

print("Participant Timings from Fastest to Slowest:" ,time)
print(*time)