S = input()
M = int(input())
substrings = []
for _ in range(M):
    substrings.append(input().split(" "))
dp = [0] * len(S)


def dfs(index):
    if index == len(S):
        return 0
    if dp[index] != 0:
        return dp[index]

    dp[index] = dfs(index + 1) + 1

    for substring in substrings:
        es, score = substring[0], int(substring[1])
        if index + len(es) <= len(S) and es == S[index : index + len(es)]:
            dp[index] = max(dp[index], dfs(index + len(es)) + score)

    return dp[index]


print(dfs(0))
