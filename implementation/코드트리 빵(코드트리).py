import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
players = set()
path = [[(0, 0)] * n for _ in range(n)]


def findBase(x, y):
    global players
    dxdy = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    queue = deque([[x, y]])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while queue:
        i, j = queue.popleft()

        if board[i][j] == 1:
            # 플레이어가 들어간 베이스캠프 위치, 원하는 편의점 위치 저장
            players.add((i, j, x, y))
            # 그리고 베이스 캠프를 못 지나가는 자리로 표시
            board[i][j] = -1
            break

        for dx, dy in dxdy:
            nx, ny = i + dx, j + dy

            if (
                0 <= nx < n
                and 0 <= ny < n
                and board[nx][ny] != -1
                and not visited[nx][ny]
            ):
                queue.append([nx, ny])
                visited[nx][ny] = True
    return


def move(p):
    pi, pj, x, y = p
    dxdy = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    queue = deque([[pi, pj]])
    visited = [[False] * n for _ in range(n)]
    visited[pi][pj] = True

    while queue:
        i, j = queue.popleft()

        if i == x and j == y:
            break

        for dx, dy in dxdy:
            nx, ny = i + dx, j + dy

            if (
                0 <= nx < n
                and 0 <= ny < n
                and board[nx][ny] != -1
                and not visited[nx][ny]
            ):
                queue.append([nx, ny])
                visited[nx][ny] = True
                path[nx][ny] = (i, j)
    i, j = x, y
    while path[i][j] != (pi, pj):
        i, j = path[i][j]
    return (i, j, x, y)


# 보드에 들어온 각 플레이어들 마다 원하는 편의점 위치의 최단거리를 향해 이동한다.
def moveAll():
    global players
    updatedPlayers = set()
    arrived = []
    for p in players:
        result = move(p)
        # 만약 플레이어가 도착했다면 그 도착 편의점 위치를 저장하고 해당 플레이어는 더 이상 저장하지 않음
        if result[0] == result[2] and result[1] == result[3]:
            arrived.append((result[0], result[1]))
        else:
            updatedPlayers.add(result)
    players = updatedPlayers
    if arrived:
        for i, j in arrived:
            board[i][j] = -1


count = 0
while count == 0 or players:
    if players:
        moveAll()
    if count <= m - 1:
        x, y = map(int, input().split())
        findBase(x - 1, y - 1)
    count += 1
print(count)
