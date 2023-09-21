N, M = map(int, input().split())


def printSequence(numbers, count, start):
    if count == M:
        print(*numbers)

    for i in range(start, N + 1):
        numbers.append(i)
        printSequence(numbers, count + 1, i + 1)
        numbers.pop()


printSequence([], 0, 1)
