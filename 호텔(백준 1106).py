C,N = map(int, input().split(" "))
INF = float('inf')
fees = []
dp = [INF]*(1101)

for _ in range(N):
    cost, ppl = map(int, input().split(" "))
    fees.append((cost, ppl))
    dp[ppl] = min(cost, dp[ppl])

for i in range(1,1101):
    for c,p in fees:
        if i-p >= 1:
            dp[i] = min(dp[i-p] + dp[p], dp[i])

print(min(dp[C:]))
#C의 최대는 1000이고 ppl은 100까지 있을 수 있기에 C를 1100까지 고려해야 최소 C를 만족하는 값들을 구할 수 있다.