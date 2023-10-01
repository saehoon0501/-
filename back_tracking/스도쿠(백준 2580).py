from copy import deepcopy

global answer


def findZeros(board):
    result = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                result.append([i, j])
    return result


def findAvailableNums(board, pos):
    x, y = pos
    row = []
    col = []
    matrix = []

    for i in range(9):
        if board[x][i] != 0:
            row.append(board[x][i])

    for i in range(9):
        if board[i][y] != 0:
            col.append(board[i][y])

    mx, my = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[mx + i][my + j] != 0:
                matrix.append(board[mx + i][my + j])

    # 가로줄에 대한 체크 & 세로줄에 대한 체크 & matrix 체크
    results = []
    for i in range(1, 10):
        if i not in row and i not in col and i not in matrix:
            results.append(i)

    return results


global success
success = False


def dfs(board, depth):
    global answer
    global success
    if depth == len(zeros):
        answer = deepcopy(board)
        success = True
        return

    available = findAvailableNums(board, zeros[depth])

    for num in available:
        x, y = zeros[depth]
        board[x][y] = num
        dfs(board, depth + 1)
        if success:
            return
        board[x][y] = 0

    return


results = []

board = [list(map(int, input().split())) for _ in range(9)]
zeros = findZeros(board)
answer = []
dfs(board, 0)

for row in answer:
    print(*row)
