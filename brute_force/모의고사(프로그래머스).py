def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []

    firstCount = 0
    secondCount = 0
    thirdCount = 0

    for i in range(len(answers)):
        answer = answers[i]
        if answer == first[i % len(first)]:
            firstCount += 1
        if answer == second[i % len(second)]:
            secondCount += 1
        if answer == third[i % len(third)]:
            thirdCount += 1

    maximum = max(firstCount, secondCount, thirdCount)
    if firstCount == maximum:
        result.append(1)
    if secondCount == maximum:
        result.append(2)
    if thirdCount == maximum:
        result.append(3)

    return result
