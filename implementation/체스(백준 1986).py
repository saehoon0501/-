N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
queenPos = list(map(int, input().split()))
knightPos = list(map(int, input().split()))
pawnPos = list(map(int, input().split()))

queenCount = queenPos[0]
queenPos = queenPos[1:]
knightCount = knightPos[0]
knightPos = knightPos[1:]
pawnCount = pawnPos[0]
pawnPos = pawnPos[1:]
global count
count = 0


def placeIt(c, pos):
    global count
    i = 0
    while i // 2 < c:
        x, y = pos[i] - 1, pos[i + 1] - 1
        if 0 <= x < N and 0 <= y < M:
            count += 1
            board[x][y] = 2
        i += 2


placeIt(queenCount, queenPos)
placeIt(knightCount, knightPos)
placeIt(pawnCount, pawnPos)

i = 0
queenMove = [[1, 0], [1, -1], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
while i // 2 < queenCount:
    x, y = queenPos[i] - 1, queenPos[i + 1] - 1
    if 0 <= x < N and 0 <= y < M:
        # Queen의 움직임을 가져와 board 내 index가 존재하는지 그리고 0인지 체크
        for dx, dy in queenMove:
            nx, ny = x + dx, y + dy
            # index가 존재할 때까지
            while 0 <= nx < N and 0 <= ny < M:
                # 보드가 0인지 체크 후 맞다면 카운트 +1 그리고 보드 1로 바꿈
                if board[nx][ny] == 0:
                    count += 1
                    board[nx][ny] = 1
                # 만약 다른 기물들이 막고 있다면 바로 멈춘다.
                elif board[nx][ny] == 2:
                    break
                # 다음 칸으로 index 증가
                nx += dx
                ny += dy
    # 다음 기물로 이동
    i += 2

i = 0
knightMove = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
while i // 2 < knightCount:
    x, y = knightPos[i] - 1, knightPos[i + 1] - 1
    if 0 <= x < N and 0 <= y < M:
        # knight의 움직임을 가져와 board 내 index가 존재하는지 그리고 0인지 체크
        for dx, dy in knightMove:
            nx, ny = x + dx, y + dy
            # index가 존재 및 보드가 0인지 체크 후 맞다면 카운트 +1 그리고 보드 1로 바꿈
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                count += 1
                board[nx][ny] = 1

    # 다음 기물로 이동
    i += 2

print(N * M - count)

## 들어가는 값이 0일 때 고려 실패함
