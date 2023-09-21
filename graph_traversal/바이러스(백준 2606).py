from collections import deque

N = int(input())
pair = int(input())
adjacents = [[] for _ in range(N + 1)]
infected = []

for _ in range(pair):
    node, adjacent = map(int, input().split())
    adjacents[node].append(adjacent)
    adjacents[adjacent].append(node)


def bfs():
    queue = deque([1])

    while len(queue) > 0:
        node = queue.pop()
        for adjacent in adjacents[node]:
            if adjacent in infected or adjacent == 1:
                continue
            infected.append(adjacent)
            queue.appendleft(adjacent)


bfs()
print(len(infected))
