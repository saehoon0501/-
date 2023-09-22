N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()


def printSequence(numbers, count):
    if count == M:
        print(*numbers)
        return

    for i in range(N):
        if sequence[i] in numbers:
            continue
        numbers.append(sequence[i])
        printSequence(numbers, count + 1)
        numbers.pop()

    return


printSequence([], 0)
