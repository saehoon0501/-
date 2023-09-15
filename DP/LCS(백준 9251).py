stringOne = input()
stringTwo = input()

dp = [[0] * (len(stringOne) + 1) for _ in range(len(stringTwo) + 1)]

for i in range(1, len(stringTwo) + 1):
    for j in range(1, len(stringOne) + 1):
        if stringTwo[i - 1] == stringOne[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(stringTwo)][len(stringOne)])
