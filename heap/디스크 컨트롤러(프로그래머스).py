from heapq import heappush, heappop


def solution(jobs):
    jobs.sort(key=lambda x: (-x[0]))
    pq = []
    print(jobs)
    results = []
    working = 0
    time = 0
    requested = 0
    while len(jobs) != 0 or len(pq) != 0 or working != 0:
        while len(jobs) > 0 and jobs[-1][0] == time:
            j = jobs.pop()
            heappush(pq, (j[1], j[0], j[1], time))
        if working == 0:
            if len(pq) > 0:
                w = heappop(pq)
                working = w[2]
                requested = w[3]
        else:
            working -= 1
            if working == 0:
                results.append(time - requested)
                if len(pq) > 0:
                    w = heappop(pq)
                    working = w[2]
                    requested = w[3]
        time += 1
    length = len(results)
    answer = sum(results) // length
    return answer
