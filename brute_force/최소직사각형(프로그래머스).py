def solution(sizes):
    maxVal = 0
    minVal = 0
    for s in sizes:
        maxS = max(s)
        minS = min(s)

        maxVal = max(maxVal, maxS)
        minVal = max(minVal, minS)

    answer = maxVal * minVal
    return answer
