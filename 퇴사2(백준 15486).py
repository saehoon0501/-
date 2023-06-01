N = int(input())
timeTable = [0]*N
priceTable = [0]*N
dp = [0]*(N+1)

for i in range(N):
    T,P = map(int,input().split(" "))
    timeTable[i] = T
    priceTable[i] = P

for i in range(N+1):    
    if i == N:
        break
    if i+timeTable[i] <= N:
        endDay = i+timeTable[i]
        dp[endDay] = max(dp[i]+priceTable[i], dp[endDay])
    
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[-1])