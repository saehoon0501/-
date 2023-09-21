import sys

sys.setrecursionlimit(10**5)

N = int(input())
adjacents = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    node, adjacent = map(int, input().split())
    adjacents[node].append(adjacent)
    adjacents[adjacent].append(node)


def dfs(node, parent):
    for adjacent in adjacents[node]:
        if not visited[adjacent]:
            visited[adjacent] = True
            dfs(adjacent, node)

    if node != 1:
        parents[node] = parent
    return


dfs(1, 0)

for i in range(2, N + 1):
    print(parents[i])
