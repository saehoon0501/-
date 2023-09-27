from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
adjacents = [[] for _ in range(10_001)]

for _ in range(M):
    a, b = map(int, input().split())
    adjacents[a].append(b)
    adjacents[b].append(a)

for i in range(1, N + 1):
    adjacents[i].sort()

global visited
visited = set()


def bfs(start, goal):
    global visited
    q = deque([[start, 0, []]])
    visited.add(start)
    while q:
        node, count, history = q.popleft()

        if node == goal:
            if count == 1:
                adjacents[start].remove(goal)
                adjacents[goal].remove(start)
            visited = set()
            for node in history:
                visited.add(node)
            return count

        for adjacent in adjacents[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                updatedHistory = history[0:]
                updatedHistory.append(adjacent)
                q.append([adjacent, count + 1, updatedHistory])
    return -1


start, goal = map(int, input().split())
result = 0
result += bfs(start, goal)
result += bfs(goal, start)

print(result)
