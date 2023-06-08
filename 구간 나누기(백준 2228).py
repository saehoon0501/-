N,M = map(int, input().split(" "))
con = [[0]+[-1e9]*M for _ in range(N+1)]
notcon = [[0]+[-1e9]*M for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min(M, (i+1)//2)+1):
        notcon[i][j] = max(con[i-1][j], notcon[i-1][j])
        con[i][j] = max(con[i-1][j], notcon[i-1][j-1])+num

print(max(notcon[N][M], con[N][M]))