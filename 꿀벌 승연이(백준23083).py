
def findAllPath(board, distance, N, M):
    global count
    odd = [(1,0),(0,1),(-1,1)]
    even = [(1,0),(0,1),(1,1)]
        
    for j in range(M):
        for i in range(N):
            if j % 2 == 0:
                for m in odd:
                    dx, dy = m
                    if 0<= i+dx < N and 0<= j+dy < M:
                        if board[i+dx][j+dy] == 0:
                            distance[i+dx][j+dy] += distance[i][j]
            else:
                for m in even:
                    dx, dy = m
                    if 0<= i+dx < N and 0<= j+dy < M:
                        if board[i+dx][j+dy] == 0:
                            distance[i+dx][j+dy] += distance[i][j]
                        
    count = distance[N-1][M-1]

global count
count = 0
N,M = map(int, input().split(" "))#N은 행수 M은 열
K = int(input())

board = [[0]*M for _ in range(N)]#NxM사이즈의 배열 생성
distance = [[0]*M for _ in range(N)]
distance[0][0] = 1

for _ in range(K):
    i,j = map(int, input().split(" "))
    board[i-1][j-1] = -1

#1,1에서 N,M까지가는 경로의 수를 구한다.
findAllPath(board, distance, N, M)
print(count%(10**9 + 7))