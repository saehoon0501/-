import sys

def input():
    return sys.stdin.readline().rstrip()

D,P = map(int, input().split(" "))
pipes = []

for _ in range(P):
    length, capacity = map(int, input().split(" "))
    pipes.append([length, capacity])

dp = [0]*(D+1)
dp[pipes[0][0]] = pipes[0][1]
for i in range(1,P):
    length, capacity = pipes[i]
    for j in range(D, (length), -1):
        if dp[j-length] > 0:
            dp[j] = max(min(dp[j-length],capacity), dp[j])        
    dp[length] = max(dp[length],capacity)

print(dp[-1])