N = int(input())
sequence = list(map(int, input().split()))
answer = 0


while True:
    done = True
    for i in range(1, len(sequence) - 1):
        if 2 * sequence[i] > sequence[i - 1] + sequence[i + 1]:
            gap = sequence[i] - (sequence[i - 1] + sequence[i + 1]) // 2
            sequence[i] -= gap
            answer += gap
            done = False
    if done:
        break

print(answer)
