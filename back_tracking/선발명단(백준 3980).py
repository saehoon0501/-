C = int(input())

global result


def dfs(depth):
    global result
    if depth == 11:
        result = max(sum(lineup), result)
        return

    for i in range(11):
        if player[depth][i] > 0 and lineup[i] == 0:
            lineup[i] = player[depth][i]
            dfs(depth + 1)
            lineup[i] = 0
    return


for _ in range(C):
    player = [list(map(int, input().split())) for _ in range(11)]
    lineup = [0] * 11
    result = 0
    dfs(0)
    print(result)
