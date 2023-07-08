N = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for cnt in range(N - 1):
    for i in range(N - cnt - 1):
        j = i + cnt + 1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j],
                dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1],
            )

print(dp[0][-1])

# 문제를 접근하는 방법을 항상 기억하자!
# 시간, 공간 복잡도 생각
# 거기에 맞는 풀이로 문제 접근
# 설계가 되면 그 이후 문제 코딩 시작
# 조건마다 반례 찾아서 집어넣어보기
