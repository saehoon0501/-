import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())#아이들의 수
children = []
dp = [1]*N
for _ in range(N):
    children.append(int(input()))

for i in range(1,N):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[j]+1,dp[i])
print(N-max(dp))

#LIS 문제