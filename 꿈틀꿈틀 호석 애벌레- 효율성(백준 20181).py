N, K = map(int, input().split(" "))
foods = list(map(int, input().split(" ")))
dp = [0] * (N + 1)
current_max = 0

# 투 포인터를 사용한다.
# 시작에서 K보다 합이 커질 때 까지 j을 +1씩 증가시킨다.
# 합이 커지면 최대값을 업데이트한 후 이를 최대 에너지를 저장하고 i를 다음 칸으로 넘어간다.
# 만약 j 포인터가 끝에 닿으면 종료 dp 중 최대 값을 가져온다.
for i in range(N):
    sum = foods[i]

    j = i + 1
    while sum < K and j < N:
        sum += foods[j]
        j += 1

    if sum >= K:
        # 연속적으로 먹은 최대값의 결과를 한칸 앞에 작성
        # 현재 칸에 저장된 최대값이 이전 칸에 저장된 최대값보다 작을 수 있기에 이를 업데이트 해야함
        current_max = max(dp[i], current_max)
        dp[j] = max(current_max + sum - K, dp[j])

    if j == N:
        break

# j가 N을 찍으면 break 하기에 최대값이 dp 끝에 찍히지 않고 중간에 작성되고 끝날 수 있다.
print(max(dp))
