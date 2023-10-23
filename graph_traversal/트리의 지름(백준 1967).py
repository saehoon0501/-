n = int(input())
adjacents = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, weight = map(int, input().split())
    adjacents[a].append((b, weight))
    adjacents[b].append((a, weight))


def dfs(i):
    stack = [(i, 0)]
    visited = [False] * (n + 1)
    result = (0, 0)
    visited[i] = True
    while stack:
        current, acc = stack.pop()
        for adjacent, weight in adjacents[current]:
            if visited[adjacent]:
                continue
            if acc + weight > result[1]:
                result = (adjacent, acc + weight)
            visited[adjacent] = True
            stack.append((adjacent, acc + weight))

    return result


mx, _ = dfs(1)
_, result = dfs(mx)

print(result)
