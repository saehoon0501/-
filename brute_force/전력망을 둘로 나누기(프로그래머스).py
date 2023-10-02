def solution(n, wires):
    answer = 101
    global adjacents

    for i in range(len(wires)):
        adjacents = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            adjacents[a].append(b)
            adjacents[b].append(a)
        visited = [False] * (n + 1)
        results = []
        for node in range(1, n + 1):
            if not visited[node]:
                results.append(dfs(visited, node))
        print(results)
        answer = min(answer, abs(results[0] - results[1]))

    return answer


def dfs(visited, node):
    result = 1
    visited[node] = True
    for adjacent in adjacents[node]:
        if not visited[adjacent]:
            result += dfs(visited, adjacent)

    return result
