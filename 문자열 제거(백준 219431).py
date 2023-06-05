def maxScore(S, substrings, dp, index):
    if index >= len(S):
        return 0
    if dp[index] != 0:
        return dp[index]
     
    dp[index] = maxScore(S, substrings, dp, index+1) + 1

    for i in range(len(substrings)):
        substring, score = substrings[i][0], int(substrings[i][1])

        if index+len(substring) <= len(S):
            if substring == S[index:index+len(substring)]:
                dp[index] = max(maxScore(S, substrings, dp, index+len(substring))+score, dp[index])
    return dp[index]

S = input()
M = int(input())
dp = [0]*len(S)
substrings = []

for _ in range(M):
    newSubstring, newScore = input().split(" ")
    substrings.append([newSubstring, newScore])
                        
maxScore(S, substrings, dp, 0)
print(dp[0])
