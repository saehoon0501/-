N = int(input())
rows = []
cols = []
for _ in range(N):
    r, c = map(int, input().split(" "))
    rows.append(r)
    cols.append(c)
dp = [[2**31 - 1] * N for _ in range(N)]

for cnt in range(N):
    for i in range(N - cnt):
        j = i + cnt
        if cnt == 0:
            dp[i][j] = 0
        else:
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j],
                    dp[i][k] + dp[k + 1][j] + rows[i] * cols[j] * cols[k],
                )

print(dp[0][-1])


# 문제를 접근하는 방법을 항상 기억하자!
# 시간, 공간 복잡도 생각
# 거기에 맞는 풀이로 문제 접근
# 설계가 되면 그 이후 문제 코딩 시작
# 조건마다 반례 찾아서 집어넣어보기
