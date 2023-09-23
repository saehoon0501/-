N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()
index = []


def printSequence(numbers, count):
    if count == M:
        print(*numbers)
        return
    PREV = 0
    for i in range(N):
        if i not in index and sequence[i] != PREV:
            numbers.append(sequence[i])
            index.append(i)
            PREV = sequence[i]
            printSequence(numbers, count + 1)
            numbers.pop()
            index.pop()

    return


printSequence([], 0)
# 중복된 수열을 체크하는 방법 유의
