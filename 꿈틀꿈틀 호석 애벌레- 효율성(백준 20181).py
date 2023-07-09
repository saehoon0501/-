N, K = map(int, input().split(" "))
stick = list(map(int, input().split(" ")))
dp = [0] * N

tmp, lmax, left, right = 0, 0, 0, 0

while True:
    if tmp >= K:
        if left == 0:
            lmax = 0
        else:
            lmax = max(lmax, dp[left - 1])
        dp[right - 1] = max(dp[right - 1], lmax + tmp - K)
        tmp -= stick[left]
        left += 1
    elif right == N:
        break
    else:
        tmp += stick[right]
        right += 1

print(max(dp))

# 투 포인터를 사용한다.
# 시작에서 K보다 합이 커질 때 까지 right을 +1씩 증가시킨다.
# 합이 커지면 최대값을 업데이트한 후 이를 최대 에너지를 저장하고 합에서 왼쪽 숫자를 빼고 다음 왼쪽 숫자로 넘어간다.
# 만약 right 포인터가 끝에 닿으면 종료 dp 중 최대 값을 가져온다.
