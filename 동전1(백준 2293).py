N, K = map(int, input().split(" "))#N은 동전 종류 K는 만들고자하는 가치
dp = [0]*(10_001)
coins = []
for _ in range(N):
    coin = int(input())    
    coins.append(coin)
dp[0] = 1
for c in coins:
    for i in range(c,10_001):
        if i-c >= 0:            
            dp[i] += dp[i-c]

print(dp[K])
#먼저 최소 코인이 만들 수 있는 가치에 +1씩 한다
#그리고 그 다음 크기 코인이 만약 최소 코인을 만들 수 있으면 거기서 +=dp[i-c]한 값을 해당 가치에 더해준다
#ex) 2원을 가지고 5를 만드는 경우 dp[3]에서 2를 더한 것이라고 생각하면 된다. dp[3]은 dp[1]에서 2를 더한 것이고~