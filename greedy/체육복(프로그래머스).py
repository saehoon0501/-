def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    tmp = []
    for i in range(len(lost)):
        l = lost[i]
        if l in reserve:
            answer += 1
            reserve.remove(l)
        else:
            tmp.append(l)

    for i in range(len(tmp)):
        l = tmp[i]
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)

    print(answer)
    return n - (len(lost) - answer)
