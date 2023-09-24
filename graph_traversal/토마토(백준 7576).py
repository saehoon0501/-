from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
riped = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            riped.append([i, j, 0])

global day
day = 0


def bfs():
    global day
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque(riped)
    while len(queue) > 0:
        x, y, count = queue.pop()
        visited[x][y] = True
        for dx, dy in dxdy:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                if board[x + dx][y + dy] == 0:
                    visited[x + dx][y + dy] = True
                    board[x + dx][y + dy] = 1
                    day = count + 1
                    queue.appendleft([x + dx, y + dy, count + 1])

    return


bfs()

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            result = -1
            break
if result == -1:
    print(result)
else:
    print(day)
