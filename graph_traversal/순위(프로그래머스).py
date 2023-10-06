def solution(n, results):
    answer = 0
    edges = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        edges[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if edges[i][k] and edges[k][j]:
                    edges[i][j] = 1

    for i in range(1, n + 1):
        count = 0
        for row in edges[i]:
            if row == 1:
                count += 1
        for j in range(1, n + 1):
            if edges[j][i] == 1:
                count += 1
        if count == n - 1:
            answer += 1
    return answer
