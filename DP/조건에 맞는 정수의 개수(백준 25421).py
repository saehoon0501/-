N = int(input())
dp = [[0] * 9 for _ in range(100_001)]
result = 0

for i in range(9):
    dp[1][i] = 1

count = 1
while count < N:
    for i in range(9):
        dp[count + 1][i] = sum(dp[count][max(0, i - 2) : min(10, i + 3)]) % 987_654_321
    count += 1
print(sum(dp[N]) % 987_654_321)
