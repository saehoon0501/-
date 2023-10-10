import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
lastAttack = [[0] * M for _ in range(N)]
attacked = [[False] * M for _ in range(N)]


def isFinished():
    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                result += 1

    return result == 1


def selectAttacker():
    result = (5001, -1, 0, 0)

    for sum in range(N + M - 2, -1, -1):
        for j in range(M - 1, -1, -1):
            i = sum - j
            if 0 > i or i >= N:
                continue

            if board[i][j] != 0:
                if board[i][j] < result[0]:
                    result = (board[i][j], lastAttack[i][j], i, j)
                elif board[i][j] == result[0]:
                    if lastAttack[i][j] > result[1]:
                        result = (board[i][j], lastAttack[i][j], i, j)
    return result[2], result[3]


def selectTarget():
    result = (-1, 1001, 0, 0)

    for sum in range(N + M - 1):
        for j in range(M):
            i = sum - j
            if 0 > i or i >= N:
                continue

            if board[i][j] != 0:
                if board[i][j] > result[0]:
                    result = (board[i][j], lastAttack[i][j], i, j)
                elif board[i][j] == result[0]:
                    if lastAttack[i][j] < result[1]:
                        result = (board[i][j], lastAttack[i][j], i, j)
    return result[2], result[3]


def tryRaser(a, t):
    come = [[None] * (M) for _ in range(N)]
    visited = [[False] * (M) for _ in range(N)]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque([a])
    visited[a[0]][a[1]] = True
    while queue:
        x, y = queue.popleft()

        for dx, dy in moves:
            nx, ny = (x + dx + N) % N, (y + dy + M) % M

            if not visited[nx][ny] and board[nx][ny] != 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                come[nx][ny] = (x, y)

    if visited[t[0]][t[1]]:
        board[t[0]][t[1]] -= board[a[0]][a[1]]
        attacked[t[0]][t[1]] = True
        x, y = t
        while x != a[0] or y != a[1]:
            x, y = come[x][y]
            if x != a[0] or y != a[1] and not attacked[x][y]:
                board[x][y] -= board[a[0]][a[1]] // 2
                attacked[x][y] = True
        return True

    return False


def bomb(a, t):
    board[t[0]][t[1]] -= board[a[0]][a[1]]
    attacked[t[0]][t[1]] = True

    moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    x, y = t
    for dx, dy in moves:
        nx, ny = (x + dx + N) % N, (y + dy + M) % M
        if board[nx][ny] != 0 and not attacked[nx][ny]:
            board[nx][ny] -= board[a[0]][a[1]] // 2
            attacked[nx][ny] = True


def repair():
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                board[i][j] = 0
            else:
                if not attacked[i][j]:
                    board[i][j] += 1
    return


count = 1
while count < K + 1:
    if isFinished():
        break
    attacked = [[False] * M for _ in range(N)]

    ax, ay = selectAttacker()
    tx, ty = selectTarget()
    board[ax][ay] += N + M
    attacked[ax][ay] = True

    if not tryRaser((ax, ay), (tx, ty)):
        bomb((ax, ay), (tx, ty))
    lastAttack[ax][ay] = count
    repair()

    count += 1

result = 0
for i in range(N):
    for j in range(M):
        result = max(board[i][j], result)
print(result)
