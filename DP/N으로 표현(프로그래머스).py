def solution(N, number):
    answer = -1
    results = []

    for i in range(1, 9):
        result = set()
        result.add(int(str(N) * i))

        for j in range(0, i - 1):
            for op1 in results[j]:
                for op2 in results[len(results) - j - 1]:
                    result.add(op1 * op2)
                    result.add(op1 + op2)
                    result.add(op1 - op2)
                    if op2 != 0:
                        result.add(op1 // op2)

        if number in result:
            answer = i
            return answer
        results.append(result)

    return answer
