N = int(input())
l = [0] * (30001)
r = [0] * (30001)
sequence = list(map(int, input().split()))

# 수열에서 등차수열을 찾기 위해 가운데 값은 idx2부터 시작하기에 먼저 왼쪽에 idx1에 해당하는 숫자 카운팅 증가
l[sequence[0]] += 1
# 그 다음 오른쪽들에 존재하는 숫자들 idx2부터 카운팅
for i in range(2, N):
    r[sequence[i]] += 1

maximumVal = max(sequence)
result = 0
# 2번째에서부터 가운데 값을 하나씩 고른다.
for i in range(1, N - 1):
    s = sequence[i]
    # 그 다음 값 기준 왼쪽과 오른쪽을 보고 j에 대응하는 숫자가 존재하는지 확인 후 둘 중 min값의 수를 결과에 반영
    for j in range(30001):
        if 1 <= s - j and s + j <= maximumVal:
            # 등차 값이 0인 경우 중복되지 않게 하나만 반영
            if s - j == s + j:
                result += l[s - j] * r[s + j]
            # 0이 아닌 경우 j에 따라 증가 또는 감소 수열을 생각할 수 있음
            else:
                result += l[s - j] * r[s + j]
                result += l[s + j] * r[s - j]
        else:
            break
    # 가운데 수열에 대한 등차수열 고르기가 끝나면 다음 수열로 넘어가기 전에 l과 r을 먼저 업데이트 한다.
    l[sequence[i]] += 1
    r[sequence[i + 1]] -= 1

print(result)
