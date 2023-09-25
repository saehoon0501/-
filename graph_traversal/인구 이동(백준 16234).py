from collections import deque
from copy import deepcopy

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
global updatedBoard
updatedBoard = deepcopy(board)
visited = []
day = 0
global count
count = 0


def bfs(start, board):
    global count
    global updatedBoard
    sum = 0
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    merge = [start]
    while queue:
        x, y = queue.popleft()
        sum += board[x][y]
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    merge.append([nx, ny])
                    count += 1

    newVal = sum // len(merge)
    for x, y in merge:
        updatedBoard[x][y] = newVal
    return


while True:
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs([i, j], board)
    if count == 0:
        print(day)
        break
    day += 1
    board = deepcopy(updatedBoard)
