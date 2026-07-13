scores = [450, 780, 620, 900, 550]

print("Original Scores:")
print(scores)

n = len(scores)

for i in range(n):
    for j in range(0, n - i - 1):
        if scores[j] < scores[j + 1]:
            temp = scores[j]
            scores[j] = scores[j + 1]
            scores[j + 1] = temp

print("Leaderboard:")
print(scores)