import math


def solution(arr):
    answer = -1
    numbers = []

    for i in range(len(arr)):
        if i % 2 == 0:
            numbers.append(int(arr[i]))

    minDp = [[10**5] * len(numbers) for _ in range(len(numbers))]
    maxDp = [[-(10**5)] * len(numbers) for _ in range(len(numbers))]

    for i in range(len(numbers)):
        minDp[i][i] = numbers[i]
        maxDp[i][i] = numbers[i]

    for cnt in range(1, len(numbers)):
        for i in range(len(numbers) - cnt):
            j = i + cnt
            if j < len(numbers):
                for k in range(i, j):
                    if arr[(k * 2) + 1] == "+":
                        maxDp[i][j] = max(maxDp[i][j], maxDp[i][k] + maxDp[k + 1][j])
                        minDp[i][j] = min(minDp[i][j], minDp[i][k] + minDp[k + 1][j])
                    else:
                        maxDp[i][j] = max(maxDp[i][j], maxDp[i][k] - minDp[k + 1][j])
                        minDp[i][j] = min(minDp[i][j], minDp[i][k] - maxDp[k + 1][j])

    answer = maxDp[0][len(numbers) - 1]
    return answer
