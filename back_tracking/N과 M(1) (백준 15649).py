N, M = map(int, input().split())

numbers = [i for i in range(1, N + 1)]

sequence = []


def printingNumbers(sequence, count, start):
    if count == M + 1:
        print(*sequence)
        return

    for i in range(1, N + 1):
        if i in sequence:
            continue
        sequence.append(i)
        printingNumbers(sequence, count + 1, i + 1)
        sequence.pop()


printingNumbers(sequence, 1, 1)
