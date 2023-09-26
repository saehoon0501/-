import sys

sys.setrecursionlimit(10**5)

n = int(input())
val = [-1] * (10_001)
visited = [False] * (10_001)
adjacents = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    adjacents[parent].append([child, weight])


def dfs(node):
    results = []
    visited[node] = True
    for c, w in adjacents[node]:
        if not visited[c]:
            results.append(dfs(c) + w)

    if len(results) == 0:
        val[node] = 0
        return 0
    results.sort(reverse=True)
    if len(results) == 1:
        val[node] = results[0]
    else:
        val[node] = results[0] + results[1]
    return max(results)


dfs(1)
print(max(val))
