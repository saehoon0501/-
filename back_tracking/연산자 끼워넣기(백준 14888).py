N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
global maximum
global minimum

maximum = -(10**9)
minimum = 10**9


def dfs(plus, minus, multi, divide, count, result):
    global maximum
    global minimum
    if count == N - 1:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    if plus > 0:
        dfs(plus - 1, minus, multi, divide, count + 1, result + numbers[count + 1])
    if minus > 0:
        dfs(plus, minus - 1, multi, divide, count + 1, result - numbers[count + 1])
    if multi > 0:
        dfs(plus, minus, multi - 1, divide, count + 1, result * numbers[count + 1])
    if divide > 0:
        if result < 0:
            dfs(
                plus,
                minus,
                multi,
                divide - 1,
                count + 1,
                -1 * ((result * -1) // numbers[count + 1]),
            )
        else:
            dfs(plus, minus, multi, divide - 1, count + 1, result // numbers[count + 1])
    return


dfs(plus, minus, multi, divide, 0, numbers[0])
print(maximum)
print(minimum)

# 문제에 주어진 조건 잘 살펴보기(뺄셈을 나눗셈할 때 어떻게 할지 정확히 안함)
