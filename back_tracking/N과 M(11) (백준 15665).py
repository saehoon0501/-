N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()


def printSequence(numbers, count):
    if count == M:
        print(*numbers)
        return
    prev = 0
    for i in range(N):
        if prev == sequence[i]:
            continue
        numbers.append(sequence[i])
        prev = sequence[i]
        printSequence(numbers, count + 1)
        numbers.pop()


printSequence([], 0)
