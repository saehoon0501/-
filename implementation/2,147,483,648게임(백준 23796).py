board = [list(map(int, input().split())) for _ in range(8)]
calculated = [[False] * 8 for _ in range(8)]


def left(board):
    for i in range(8):
        for j in range(1, 8):
            if board[i][j] > 0:
                k = 1
                # 앞에 벽이나 숫자가 있는 칸이 아닐 때까지 왼쪽으로 칸을 이동
                while 0 < j - k and board[i][j - k] == 0:
                    k += 1
                if board[i][j - k] != 0:
                    # 만약 칸에 존재하는 숫자가 이동 칸과 같은 경우 그리고 아직 합져지지 않은 경우
                    if board[i][j - k] == board[i][j] and not calculated[i][j - k]:
                        board[i][j - k] += board[i][j]
                        calculated[i][j - k] = True
                        board[i][j] = 0
                    else:
                        board[i][j - k + 1] = board[i][j]
                        if k != 1:
                            board[i][j] = 0
                # 그 외 벽인 경우
                else:
                    board[i][j - k] = board[i][j]
                    board[i][j] = 0

    return


def up(board):
    for j in range(8):
        for i in range(1, 8):
            if board[i][j] > 0:
                k = 1
                # 앞에 벽이나 숫자가 있는 칸이 아닐 때까지 오른쪽으로 칸을 이동
                while 0 < i - k and board[i - k][j] == 0:
                    k += 1
                if board[i - k][j] != 0:
                    # 만약 칸에 존재하는 숫자가 이동 칸과 같은 경우 그리고 아직 합져지지 않은 경우
                    if board[i - k][j] == board[i][j] and not calculated[i - k][j]:
                        board[i - k][j] += board[i][j]
                        calculated[i - k][j] = True
                        board[i][j] = 0
                    else:
                        board[i - k + 1][j] = board[i][j]
                        if k != 1:
                            board[i][j] = 0
                # 그 외 벽인 경우
                else:
                    board[i - k][j] = board[i][j]
                    board[i][j] = 0

    return


def right(board):
    for i in range(8):
        for j in range(6, -1, -1):
            if board[i][j] > 0:
                k = 1
                # 앞에 벽이나 숫자가 있는 칸이 아닐 때까지 오른쪽으로 칸을 이동
                while j + k < 7 and board[i][j + k] == 0:
                    k += 1
                if board[i][j + k] != 0:
                    # 만약 칸에 존재하는 숫자가 이동 칸과 같은 경우 그리고 아직 합져지지 않은 경우
                    if board[i][j + k] == board[i][j] and not calculated[i][j + k]:
                        board[i][j + k] += board[i][j]
                        calculated[i][j + k] = True
                        board[i][j] = 0
                    else:
                        board[i][j + k - 1] = board[i][j]
                        if k != 1:
                            board[i][j] = 0
                # 그 외 벽인 경우
                else:
                    board[i][j + k] = board[i][j]
                    board[i][j] = 0

    return


def down(board):
    for j in range(8):
        for i in range(6, -1, -1):
            if board[i][j] > 0:
                k = 1
                # 앞에 벽이나 숫자가 있는 칸이 아닐 때까지 오른쪽으로 칸을 이동
                while i + k < 7 and board[i + k][j] == 0:
                    k += 1
                if board[i + k][j] != 0:
                    # 만약 칸에 존재하는 숫자가 이동 칸과 같은 경우 그리고 아직 합져지지 않은 경우
                    if board[i + k][j] == board[i][j] and not calculated[i + k][j]:
                        board[i + k][j] += board[i][j]
                        calculated[i + k][j] = True
                        board[i][j] = 0
                    else:
                        board[i + k - 1][j] = board[i][j]
                        if k != 1:
                            board[i][j] = 0
                # 그 외 벽인 경우
                else:
                    board[i + k][j] = board[i][j]
                    board[i][j] = 0

    return


cmd = input()

if cmd == "U":
    up(board)
elif cmd == "L":
    left(board)
elif cmd == "R":
    right(board)
else:
    down(board)

for row in board:
    print(*row)
