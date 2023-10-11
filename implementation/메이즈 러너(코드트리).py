import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
board = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0] * N for _ in range(N)]
players = []
for _ in range(M):
    i, j = map(int, input().split())
    players.append((i - 1, j - 1))
exit = tuple(map(int, input().split()))
global count
count = 0
# 미로의 벽은 -값으로 플레이어는 그 수 그리고 출구는 -10값으로 같이 저장한다.
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            matrix[i][j] = -1 * board[i][j]

for i, j in players:
    matrix[i][j] += 1

matrix[exit[0] - 1][exit[1] - 1] = -10


def findExit():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == -10:
                return (i, j)


def moveAll():
    global count
    exit = findExit()
    newMatrix = [[0] * N for _ in range(N)]
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(N):
        for j in range(N):
            # 만약 벽이거나 출구면 그냥 복사 후 지나감
            if matrix[i][j] < 0:
                newMatrix[i][j] = matrix[i][j]
                continue
            # 현재 위치에서의 출구 거리
            currentDist = abs(exit[0] - i) + abs(exit[1] - j)
            moved = False
            for dx, dy in dxdy:
                nx, ny = i + dx, j + dy
                # 이동할 수 있는 칸인지 먼저 확인
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] >= 0:
                        minDist = abs(exit[0] - nx) + abs(exit[1] - ny)
                        # 이동 가능한 칸이면 현재 위치보다 출구에 더 가까워지는지 확인
                        if minDist < currentDist:
                            # 해당 칸 인원들 모두 이동
                            count += matrix[i][j]
                            newMatrix[nx][ny] += matrix[i][j]
                            moved = True
                            break
                    elif matrix[nx][ny] == -10:
                        count += matrix[i][j]
                        moved = True
                        continue
            if not moved:
                newMatrix[i][j] += matrix[i][j]
    return newMatrix


def isFinished():
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 0:
                count += 1

    return count == 0


def findSquare():
    exit = findExit()
    result = 1000
    # 플레이어로부터 출구까지의 최단거리를 구해 최소 정사각형 길이를 구한다.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 0:
                dist = max(abs(exit[0] - i), abs(exit[1] - j)) + 1
                result = min(result, dist)

    si, sj = -1, -1
    # 구해진 정사각형 길이를 이용해 정사각형 찾기
    for i in range(N - result + 1):
        for j in range(N - result + 1):
            exitFound, playerFound = False, False
            for r in range(i, i + result):
                for c in range(j, j + result):
                    if matrix[r][c] == -10:
                        exitFound = True
                    elif matrix[r][c] > 0:
                        playerFound = True
                    if exitFound and playerFound:
                        si, sj = i, j
                        break
            if si != -1:
                break
        if si != -1:
            break
    return si, sj, result


def rotate():
    i, j, dist = findSquare()
    tmp = [[0] * (dist) for _ in range(dist)]
    rotated = [[0] * (dist) for _ in range(dist)]
    # 임시 배열로 옮긴 후 시계방향 90도 회전시킨다.
    for x in range(i, i + dist):
        for y in range(j, j + dist):
            tmp[x - i][y - j] = matrix[x][y]

    for x in range(dist):
        for y in range(dist):
            if tmp[x][y] < 0 and tmp[x][y] != -10:
                tmp[x][y] += 1
            rotated[y][dist - 1 - x] = tmp[x][y]

    for x in range(dist):
        for y in range(dist):
            matrix[x + i][y + j] = rotated[x][y]

    return


sec = 0
while sec < K:
    matrix = moveAll()
    if isFinished():
        break
    rotate()
    sec += 1

exit = findExit()
print(count)
print(exit[0] + 1, exit[1] + 1)
