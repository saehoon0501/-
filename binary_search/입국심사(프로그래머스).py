def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n

    while l <= r:
        count = 0
        mid = (l + r) // 2
        for t in times:
            count += mid // t
            if count > n:
                break

        if count >= n:
            r = mid - 1
            answer = mid
        elif count < n:
            l = mid + 1

    return answer
