T = int(input())
results = []

for _ in range(T):    
    N = int(input())        
    coins = list(map(int, input().split(" ")))            
    M = int(input())    
    dp = [0]*(M+1)
    dp[0] = 1
    
    for c in coins:
        for i in range(c,(M+1)):
            if i-c >= 0:
                dp[i] += dp[i-c]
    
    results.append(dp[M])

for r in results:
    print(r)