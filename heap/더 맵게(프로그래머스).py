from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K and len(scoville) > 1:
        a = heappop(scoville)
        b = heappop(scoville)

        result = a + b * 2
        heappush(scoville, result)
        answer += 1

    if len(scoville) == 0 or (len(scoville) == 1 and scoville[0] < K):
        return -1

    return answer
