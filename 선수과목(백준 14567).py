N, M = map(int, input().split())
dp = [1] * (N + 1)
courses = [list(map(int, input().split())) for _ in range(M)]
courses.sort(key=lambda x: (x[0], x[1]))

for i in range(M):
    a, b = courses[i]
    dp[b] = max(dp[a] + 1, dp[b])

print(*dp[1:])
