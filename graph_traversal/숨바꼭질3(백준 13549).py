import sys

sys.setrecursionlimit(10**5)

N, K = map(int, input().split())
visited = [False] * (K + 1)


def dfs(pos, count):
    result = K + 1
    if pos == K:
        return count
    if 0 <= pos - 1 < K + 1 and not visited[pos - 1]:
        visited[pos - 1] = True
        result = min(dfs(pos - 1, count + 1), result)
        visited[pos - 1] = False
    if 0 <= pos + 1 < K + 1 and not visited[pos + 1]:
        visited[pos + 1] = True
        result = min(dfs(pos + 1, count + 1), result)
        visited[pos + 1] = False
    if 0 <= 2 * pos < K + 1 and not visited[2 * pos]:
        visited[2 * pos] = True
        result = min(dfs(2 * pos, count), result)
        visited[2 * pos] = False

    return result


visited[N] = True
result = dfs(N, 0)
print(result)
