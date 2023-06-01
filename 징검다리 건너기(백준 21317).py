N = int(input())
INF = float('inf')
jumps = [[0]*2 for _ in range(N-1)]
rocks = [INF for _ in range(N)]
for i in range(N-1):
    little, big = map(int, input().split(" "))
    jumps[i][0] = little
    jumps[i][1] = big

K = int(input())
rocks[0] = 0
for i in range(N):
    if i+1 <= N-1:
        rocks[i+1] = min(rocks[i+1],jumps[i][0] + rocks[i])
    if i+2 <= N-1:
        rocks[i+2] = min(rocks[i+2],jumps[i][1] + rocks[i])

_min = rocks[-1]
for i in range(3, N):
    e, dp1, dp2 = rocks[i-3]+K, INF, INF
    for j in range(i, N-1):
        if i+1<=N : dp1 = min(dp1, e+jumps[j][0])
        if i+2<=N : dp2 = min(dp2, e+jumps[j][1])
        e, dp1, dp2 = dp1, dp2, INF
    _min = min(_min, e)

print(_min)
#딱 한번 할 수 있는 수퍼 점프가 반영되면 이전에 했던 이후 모든 결과들을 수정해줘야한다
#이유는 점화식으로 구한 결과들은 1,2 칸에서 움직임만을 고려했기에 3칸 움직임이 반영되면 기존 결과가 싹다 바뀌기 때문