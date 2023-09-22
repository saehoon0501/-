N, M = map(int, input().split())


def printSequence(numbers, count, start):
    if count == M:
        print(*numbers)
        return

    for i in range(start, N + 1):
        numbers.append(i)
        printSequence(numbers, count + 1, i)
        numbers.pop()
    return


printSequence([], 0, 1)
