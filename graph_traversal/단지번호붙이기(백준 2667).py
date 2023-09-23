from collections import deque

N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    row = input()
    for j in range(N):
        board[i].append(int(row[j]))
visited = [[False] * N for _ in range(N)]

global count


def bfs(start):
    global count
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while len(queue) > 0:
        x, y = queue.pop()
        for dx, dy in dxdy:
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if visited[x + dx][y + dy] == False and board[x + dx][y + dy] == 1:
                    count += 1
                    visited[x + dx][y + dy] = True
                    queue.appendleft([x + dx, y + dy])
    return count


results = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and board[i][j] == 1:
            count = 1
            results.append(bfs([i, j]))

print(len(results))
results.sort()
for r in results:
    print(r)
