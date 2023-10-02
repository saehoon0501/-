import math


def isPrime(num):
    if num == 0 or num == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(num)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if num % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def dfs(num, numbers, selected):
    global results
    global answer
    if num != "":
        prime = int(num)
        if prime not in results and isPrime(prime):
            answer += 1
            results.add(prime)

    for i in range(len(numbers)):
        if i not in selected:
            selected.append(i)
            dfs("".join([num, numbers[i]]), numbers, selected)
            selected.pop()
    return


def solution(numbers):
    global results
    global answer
    answer = 0
    results = set()

    dfs("", numbers, [])

    return answer
