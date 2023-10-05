def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    l, r = 1, distance

    while l <= r:
        count = 0
        mid = (l + r) // 2

        prev = 0
        for i in range(len(rocks)):
            gap = rocks[i] - prev
            if gap < mid:
                count += 1
                if count > n:
                    break
                continue
            prev = rocks[i]

        gap = distance - prev
        if gap < mid:
            count += 1

        if count > n:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid

    return answer
