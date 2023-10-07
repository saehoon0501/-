T = int(input())
N = 0


def dfs(expression, depth):
    if depth == N + 1:
        if readExpression(expression) == 0:
            answer.append(expression)
        return
    # 더하기
    dfs("".join([expression, "+", str(depth)]), depth + 1)
    # 공백
    dfs("".join([expression, " ", str(depth)]), depth + 1)
    # 빼기
    dfs("".join([expression, "-", str(depth)]), depth + 1)

    return


def readExpression(expression):
    tmp = expression.replace(" ", "")
    tmp = tmp.replace("+", " ").replace("-", " ")
    numbers = list(map(int, tmp.split(" ")))

    i = 1
    result = numbers[0]
    count = 1
    while i < len(expression) and count < len(numbers):
        if expression[i] == "+":
            result += numbers[count]
            count += 1
        elif expression[i] == "-":
            result -= numbers[count]
            count += 1
        i += 1

    return result


global answer
for _ in range(T):
    N = int(input())
    answer = []
    dfs("1", 2)
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
    print()
