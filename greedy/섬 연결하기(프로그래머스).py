from heapq import heappop, heappush


def solution(n, costs):
    heap = []
    answer = 0
    adjacents = [[] for _ in range(n)]

    if n == 1:
        return answer

    for a, b, c in costs:
        adjacents[a].append([b, c])
        adjacents[b].append([a, c])

    visited = [False] * (n)

    for adjacent, cost in adjacents[0]:
        heappush(heap, (cost, adjacent))
    visited[0] = True

    while heap:
        minimumCost, node = heappop(heap)
        if not visited[node]:
            visited[node] = True
            answer += minimumCost
            for adjacent, cost in adjacents[node]:
                if not visited[adjacent]:
                    heappush(heap, (cost, adjacent))

    return answer
