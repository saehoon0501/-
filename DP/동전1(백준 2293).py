n, k = map(int, input().split())
dp = [0] * (k + 1)
coins = []

for _ in range(1, n + 1):
    coin = int(input())
    if coin in coins or k < coin:
        coins.append(coin)
        continue
    else:
        coins.append(coin)
        for j in range(k + 1):
            if j == coin:
                dp[j] += 1
            elif j > coin:
                dp[j] += dp[j - coin]

print(dp[k])
# 메로리 제한 조건 체크 안함
