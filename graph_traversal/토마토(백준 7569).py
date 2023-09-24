from collections import deque

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
riped = []

for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 1:
                riped.append([h, i, j, 0])

global day
day = 0


def bfs():
    global day
    dhdxdy = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    queue = deque(riped)

    while len(queue) > 0:
        h, x, y, count = queue.pop()
        visited[h][x][y] = True
        for dh, dx, dy in dhdxdy:
            if 0 <= h + dh < H and 0 <= x + dx < N and 0 <= y + dy < M:
                if (
                    board[h + dh][x + dx][y + dy] == 0
                    and not visited[h + dh][x + dx][y + dy]
                ):
                    visited[h + dh][x + dx][y + dy] = True
                    board[h + dh][x + dx][y + dy] = 1

                    day = count + 1
                    queue.appendleft([h + dh, x + dx, y + dy, count + 1])
    return


bfs()

result = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 0:
                result = -1
                break

if result == -1:
    print(result)
else:
    print(day)
