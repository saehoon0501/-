N = int(input())
eggs = [0] * N
weights = [0] * N
global result
result = 0

for i in range(N):
    durability, weight = map(int, input().split())
    eggs[i] = durability
    weights[i] = weight


def dfs(selected):
    global result
    if selected == N:
        count = 0
        for e in eggs:
            if e <= 0:
                count += 1
        result = max(result, count)
        return

    left = N
    for e in eggs:
        if e <= 0:
            left -= 1

    if eggs[selected] > 0 and left > 1:
        for i in range(N):
            w1, w2 = weights[selected], weights[i]
            if eggs[i] > 0 and i != selected:
                eggs[selected] -= w2
                eggs[i] -= w1
                dfs(selected + 1)
                eggs[selected] += w2
                eggs[i] += w1
    else:
        dfs(selected + 1)
    return


dfs(0)
print(result)
