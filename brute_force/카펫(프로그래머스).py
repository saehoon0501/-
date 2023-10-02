def solution(brown, yellow):
    answer = []
    # i는 세로 길이, j는 가로 길이
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            print(i, j)
            if i * j == yellow:
                if i + j == (brown - 4) // 2:
                    answer = [j + 2, i + 2]
        if len(answer) != 0:
            break
    return answer
