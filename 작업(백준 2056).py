import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dp = [0]*N
for k in range(N):
    tmp = input().split(" ")
    
    cost = int(tmp[0])
    priority = int(tmp[1])
    
    if priority >= 1:
        for i in range(2,priority+2):
            dp[k] = max(dp[int(tmp[i])-1], dp[k])
        dp[k] += cost
    else:
        dp[k] = cost
print(max(dp))