N, S = map(int, input().split())
sequence = list(map(int, input().split()))


def dfs(numbers, start):
    result = 0
    if len(numbers) != 0 and sum(numbers) == S:
        result += 1

    for i in range(start, N):
        numbers.append(sequence[i])
        result += dfs(numbers, i + 1)
        numbers.pop()

    return result


print(dfs([], 0))

# 가장 간단하게 푸는 것이 오류를 최소화할 수 있는 방법
# 부분수열은 꼭 연속적이여야 하는 것이 아니다.
