N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()


def printSequence(numbers, count, start):
    if count == M:
        print(*numbers)
        return

    for i in range(start, N):
        numbers.append(sequence[i])
        printSequence(numbers, count + 1, i)
        numbers.pop()
    return


printSequence([], 0, 0)
