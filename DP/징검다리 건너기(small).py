def canDo(i,j,jumps,K):
    return (j-i)*(1+abs(jumps[i] - jumps[j])) <= K

N,K = map(int, input().split(" "))
jumps = list(map(int, input().split(" ")))
dp = [0]*N
dp[0] = 1
for i in range(N):
    if dp[i] != 1:
        continue
    start = i+1
    for j in range(start,N):
        if canDo(i,j,jumps,K):
            dp[j] = 1
    if dp[-1] == 1:
        break

if dp[-1] == 1:
    print("YES")
else:
    print("NO")