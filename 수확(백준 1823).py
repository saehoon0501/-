import sys


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


input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())
rice = [int(input()) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


print(get_maxvalue(0, n - 1, 1))
# top-down 접근을 통해 Left에서 시작해 Right까지 최대 합 + 선택된 숫자 결과를 가져온다.
# 이러한 중간 결과들을 모두 dp에 저장하면된다.
