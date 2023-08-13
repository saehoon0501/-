D, P = map(int, input().split(" "))
pipes = []
dp = [0] * (100001)
for _ in range(P):
    pipes.append(list(map(int, input().split(" "))))
l, c = pipes[0]
dp[l] = c

for i in range(1, P):
    l, c = pipes[i]
    for j in range(D, l, -1):
        if dp[j - l] > 0:
            dp[j] = max(min(dp[j - l], c), dp[j])
    dp[l] = max(c, dp[l])

print(dp[D])
