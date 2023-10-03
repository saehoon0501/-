def solution(name):
    global az
    az = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 12,
        "P": 11,
        "Q": 10,
        "R": 9,
        "S": 8,
        "T": 7,
        "U": 6,
        "V": 5,
        "W": 4,
        "X": 3,
        "Y": 2,
        "Z": 1,
    }
    global change
    change = 0
    for i in range(len(name)):
        if i != 0 and name[i] != "A":
            change += 1
    global visited
    visited = [False] * len(name)
    visited[0] = True
    global answer
    answer = 10**4
    moveSlot(0, name, 0, 0)
    return answer


def moveSlot(currentPos, name, result, depth):
    global az
    global change
    global answer

    # 현재 문자가 A가 아니라면 A에서 해당 문자로 변경하는 횟수를 더한다.
    result += az[name[currentPos]]

    if depth == change:
        answer = min(answer, result)
        return
    # 그리고 A가 아닌 다음 가장 가까운 칸을 계산한다.
    nearest = []
    i = (currentPos + 1) % len(name)
    count = 1
    while i != currentPos:
        if name[i] != "A" and not visited[i]:
            visited[i] = True
            moveSlot(i, name, result + count, depth + 1)
            visited[i] = False
            break
        i = (i + 1) % len(name)
        count += 1

    i = currentPos - 1
    count = 1
    while i != currentPos:
        if i == -1:
            i = len(name) - 1
            continue
        if name[i] != "A" and not visited[i]:
            visited[i] = True
            moveSlot(i, name, result + count, depth + 1)
            visited[i] = False
            break
        i -= 1
        count += 1

    return
