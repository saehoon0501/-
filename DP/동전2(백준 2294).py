n, k = map(int, input().split())
dp = [10**5] * (k + 1)

for _ in range(n):
    coin = int(input())
    if coin <= k:
        dp[coin] = 1
        for j in range(coin + 1, k + 1):
            if dp[j - coin] != 10**5:
                dp[j] = min(dp[j - coin] + 1, dp[j])
if dp[k] == 10**5:
    print(-1)
else:
    print(dp[k])

# 10**4으로 초기화했기에 그에 해당하는 경우 제대로된 결과가 나오지 않았음
