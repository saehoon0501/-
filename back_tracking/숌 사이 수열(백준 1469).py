N = int(input())
numbers = list(map(int, input().split()))
counter = [0] * (17)

global answer
answer = []
numbers.sort()


def dfs(selected, depth):
    global answer
    if depth == 2 * N:
        if len(answer) == 0:
            answer = selected[0:]
            return
        return

    for s in selected:
        if counter[s] == s:
            for i in selected:
                counter[i] += 1
            selected.append(s)
            dfs(selected, depth + 1)
            selected.pop()
            for i in selected:
                counter[i] -= 1
            return

    for num in numbers:
        if num in selected:
            continue

        for s in selected:
            counter[s] += 1
        selected.append(num)
        dfs(selected, depth + 1)
        selected.pop()
        for s in selected:
            counter[s] -= 1
    return


dfs([], 0)
if len(answer) > 0:
    print(*answer)
else:
    print(-1)

# 문제 풀이 후 작성했던 조건들 하나하나 주석을 달며 체크해야 할듯
