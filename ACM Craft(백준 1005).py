from collections import deque

T = int(input())
answer = []
for _ in range(T):
    N, K = map(int, input().split(" "))
    times = list(map(int, input().split(" ")))
    dp = [0] * N
    cnt = [0] * N
    orders = [[] for _ in range(N)]
    for _ in range(K):
        former, later = map(int, input().split(" "))
        orders[former - 1].append(later - 1)
        cnt[later - 1] += 1
    W = int(input())

    queue = deque()
    for i in range(N):
        if cnt[i] == 0:
            queue.append(i)
            dp[i] = times[i]

    while len(queue) > 0:
        curNode = queue.popleft()
        for node in orders[curNode]:
            dp[node] = max(dp[curNode] + times[node], dp[node])
            cnt[node] -= 1
            if cnt[node] == 0:
                queue.append(node)
        if cnt[W - 1] == 0:
            answer.append(dp[W - 1])
            break

print(*answer, sep="\n")

# 위상정렬을 도입해 Dependency가 없는 순서대로 DP를 수행한다.
