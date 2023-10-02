def dfs(energy, finished, dungeons):
    global answer
    if len(finished) != 0:
        answer = max(answer, len(finished))

    for i in range(len(dungeons)):
        if i not in finished:
            required, depeleted = dungeons[i]
            if energy >= required:
                finished.append(i)
                dfs(energy - depeleted, finished, dungeons)
                finished.pop()
    return


def solution(k, dungeons):
    global answer
    answer = 0
    dfs(k, [], dungeons)

    return answer
