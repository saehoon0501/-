N,K = map(int, input().split(" "))
coins = []
INF = float('inf')
dp = [INF]*(100_001)

for _ in range(N):
    coin = int(input())
    if coin in coins:
        continue
    dp[coin] = 1
    coins.append(coin)

for c in coins:
    for i in range(c,10_001):
        if i-c >= 0:
            dp[i] = min(dp[i-c] + 1, dp[i])

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])

#동전의 가치는 100_000까지 가능하기에 그만큼의 배열을 만든다.
#하지만 K는 10_001만큼이기에 loop 범위는 거기까지만 계산하면 된다
#그리고 결과 출력 조건을 자세히 살펴봐야한다