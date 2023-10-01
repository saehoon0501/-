from heapq import heappop, heappush


def getMin(minPQ, maxPQ):
    result = heappop(minPQ)
    maxPQ.remove(-result)
    return result


def getMax(minPQ, maxPQ):
    result = heappop(maxPQ)
    minPQ.remove(-result)
    return -result


def solution(operations):
    minPQ = []
    maxPQ = []
    answer = []
    result = 0
    for op in operations:
        instruction, val = op.split(" ")

        if instruction == "I":
            heappush(minPQ, int(val))
            heappush(maxPQ, -int(val))
        elif instruction == "D" and val == "-1":
            if len(minPQ) > 0:
                getMin(minPQ, maxPQ)
        else:
            if len(maxPQ) > 0:
                getMax(minPQ, maxPQ)

    a, b = 0, 0
    if len(minPQ) > 1:
        a = getMax(minPQ, maxPQ)
        b = getMin(minPQ, maxPQ)
    elif len(minPQ) == 1:
        a = getMin(minPQ, maxPQ)
        b = a
    answer = [a, b]
    return answer
