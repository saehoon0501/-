N, M, H = map(int, input().split(" "))#N 인원 수, M 인당 최대 블록, H 만들고자하는 탑 높이
blocks = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0]*(H+1)for _ in range(N)]
dp[0][0] = 1
for block in blocks[0]:
    dp[0][block] = 1

for i in range(1,N):
    for b in range((len(blocks[i])+1)):
        block = 0
        if b > 0:
            block = blocks[i][b-1]
            for j in range((H+1)):
                if dp[i-1][j] >= 1:
                    if block + j <= H:
                        dp[i][block + j] += dp[i-1][j]
        else:
            for j in range((H+1)):                                    
                dp[i][block + j] = dp[i-1][block+j]

print(dp[N-1][-1]%10_007)