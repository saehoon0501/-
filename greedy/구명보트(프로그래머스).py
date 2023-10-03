def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l = 0
    r = len(people) - 1

    while l < r:
        sum = people[l] + people[r]

        if sum > limit:
            l += 1
        else:
            l += 1
            r -= 1

        answer += 1

    if l == r:
        answer += 1
    return answer
