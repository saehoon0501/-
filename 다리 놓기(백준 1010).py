import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

dp = [[0]*31 for _ in range(31)]
dp[0][0] = 1

for num in range(1,31):
    dp[num][0] = 1
    for pick in range(1,31):
        dp[num][pick] = dp[num-1][pick] + dp[num-1][pick-1]

for _ in range(T):
    N,M = map(int, input().split(" "))
    print(dp[M][N])