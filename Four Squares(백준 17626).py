dp = [5] * 50001

n = int(input())
dp[1] = 1
for i in range(2, 50001):
    count = 1
    while count**2 <= i:
        if i == count**2:
            dp[i] = 1
        else:
            dp[i] = min(dp[i - count**2] + 1, dp[i])
        count += 1

print(dp[n])

# 시간 초과 안나네??
