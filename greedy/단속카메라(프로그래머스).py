def solution(routes):
    answer = 0

    routes.sort(key=lambda x: (x[1]))

    stanEntry, stanExit = routes[0]
    camera = stanExit
    i = 1
    while i < len(routes):
        cmpEntry, cmpExit = routes[i]

        if camera < cmpEntry:
            answer += 1
            camera = cmpExit
        i += 1

    return answer + 1
