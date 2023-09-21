from collections import deque

N, M, V = map(int, input().split())
adjacents = [[] for _ in range(N + 1)]
for _ in range(M):
    first, second = map(int, input().split())
    adjacents[first].append(second)
    adjacents[second].append(first)

for i in range(1, N + 1):
    adjacents[i].sort()


def dfs(node, visited):
    for adjacent in adjacents[node]:
        if adjacent not in visited:
            visited.append(adjacent)
            dfs(adjacent, visited)
    return visited


def bfs():
    queue = deque([V])
    visited = [V]
    while len(queue) > 0:
        node = queue.pop()
        for adjacent in adjacents[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.appendleft(adjacent)
    return visited


print(*dfs(V, [V]))
print(*bfs())
