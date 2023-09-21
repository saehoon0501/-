N, M = map(int, input().split())


def printSequence(numbers, count):
    if count == M:
        print(*numbers)
        return

    for i in range(1, N + 1):
        numbers.append(i)
        printSequence(numbers, count + 1)
        numbers.pop()
    return


printSequence([], 0)
