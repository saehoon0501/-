N, M = map(int, input().split())
board = [[0] * (M + 2) for _ in range(N + 2)]

global count
count = 0


def dfs(level):
    global count
    if level == N * M:
        count += 1
        return
    # 2D 배열을 for문 없이 이동하는 방법
    x = level // M + 1
    y = level % M + 1

    # 현재 칸에 놓을 수 있을 경우 넴모를 놓는 경우
    if board[x - 1][y] == 0 or board[x][y - 1] == 0 or board[x - 1][y - 1] == 0:
        board[x][y] = 1
        dfs(level + 1)
        board[x][y] = 0
    # 현재 칸에 넴모를 놓지 않는 경우
    dfs(level + 1)


dfs(0)
print(count)

# 모든 칸마다 넴모를 놓는 경우와 그렇지 않은 경우 2가지로 나눠 가능한 조합의 모든 경우를 볼 수 있다.
# level은 각 칸을 의미한다. 따라서 최대 level은 칸의 최대 수인 N*M까지 가능하다.
