import sys

input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())
rice = [int(input()) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


def get_maxvalue(s, e, cnt):
    # base case
    if s == e:
        return cnt * rice[s]
    if dp[s][e]:
        return dp[s][e]
    # step
    dp[s][e] = max(
        get_maxvalue(s + 1, e, cnt + 1) + cnt * rice[s],
        get_maxvalue(s, e - 1, cnt + 1) + cnt * rice[e],
    )
    return dp[s][e]


print(get_maxvalue(0, n - 1, 1))
