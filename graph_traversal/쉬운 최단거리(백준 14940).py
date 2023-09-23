from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
distances = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = [i, j, 0]
            break


def bfs(start):
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while len(queue) > 0:
        x, y, count = queue.pop()
        for dx, dy in dxdy:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if visited[x + dx][y + dy] == False and board[x + dx][y + dy] != 0:
                    visited[x + dx][y + dy] = True
                    distances[x + dx][y + dy] = count + 1
                    queue.appendleft([x + dx, y + dy, count + 1])
    return


bfs(start)

for i in range(n):
    for j in range(m):
        if distances[i][j] == 0 and board[i][j] == 1:
            distances[i][j] = -1

for row in distances:
    print(*row)
