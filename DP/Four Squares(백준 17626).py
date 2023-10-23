N = int(input())
dp = [0] * 50001

i = 1
while i**2 < 50000:
    dp[i**2] = 1
    i += 1

j = 0
for i in range(1, N + 1):
    if (j + 1) ** 2 == i:
        j += 1
    if dp[i] == 0:
        mn = 5
        cnt = j
        while cnt > 0:
            mn = min(mn, dp[i - (cnt**2)])
            cnt -= 1
        dp[i] = mn + 1


print(dp[N])
