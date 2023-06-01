import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split(" "))#N 과목 수, M 선수 조건의 수
dp = [1]*(N+1)
pres = []
for _ in range(M):
    a,b = map(int, input().split(" "))# a < b 선수과목
    pres.append([a,b])

pres.sort(key=lambda x:(x[0],x[1]))

for a,b in pres:
    dp[b] = max(dp[b], dp[a]+1)

for result in dp[1:]:
    print(result, end=" ")
print()