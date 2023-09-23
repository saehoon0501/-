N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
global start


def dfs(prev, sum, count):
    global start
    if count == N - 1:
        if W[prev][start] != 0:
            return sum + W[prev][start]
        else:
            return 10**8
    result = 10**8
    for i in range(N):
        if visited[i] == False and W[prev][i] != 0:
            visited[i] = True
            result = min(dfs(i, sum + W[prev][i], count + 1), result)
            visited[i] = False
    return result


results = []
for i in range(N):
    start = i
    visited[i] = True
    results.append(dfs(i, 0, 0))
    visited[i] = False

print(min(results))

# 마지막에 돌아갈 때 돌아갈 수 있는 경우가 아닌 케이스를 빼먹음
