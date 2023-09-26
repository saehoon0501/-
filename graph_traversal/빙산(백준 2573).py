from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
newBoard = deepcopy(board)


def bfs(start):
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque([start])
    visited.add((start[0], start[1]))

    while q:
        i, j = q.popleft()
        for dx, dy in dxdy:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                # 만약 주변에 칸이 0이라면 복사된 배열에 -1
                if board[nx][ny] == 0:
                    if newBoard[i][j] > 0:
                        newBoard[i][j] -= 1
                # 주변 칸이 1이라면 visited 처리 후 큐에 넣는다.
                else:
                    visited.add((nx, ny))
                    q.append([nx, ny])


year = 0
visited = set()
while True:
    iceberg = []
    # 배열 전체를 스캔하여 숫자가 있는 부분 저장
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] != 0:
                iceberg.append([i, j])

    if len(iceberg) == 0:
        break
    count = 0
    visited.clear()
    # iceberg에 있는 위치들에 대해 bfs를 호출한다. visited 처리가 되었다면 이는 수행하지 않는다.
    # bfs를 호출하는 횟수를 카운트하여 빙산의 개수를 저장한다.
    for i, j in iceberg:
        if (i, j) not in visited:
            bfs([i, j])
            count += 1

    if count >= 2:
        break
    board = deepcopy(newBoard)
    year += 1


if count >= 2:
    print(year)
else:
    print(0)
