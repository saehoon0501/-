A, B = map(str, input().split())

count = 0
while True:
    # B를 A로 만들 수 있으면 성공
    if int(B) == int(A):
        print(count + 1)
        break
    # B가 A보다 작을 때까지 성공 못하면 끝남
    elif int(B) < int(A):
        print(-1)
        break

    lastDigit = int(B[-1])
    # 짝수이면 2로 나눈다.
    if lastDigit % 2 == 0:
        B = str(int(B) // 2)
        count += 1
    # 1이면 그 자리를 제거한다.
    elif lastDigit == 1:
        B = B[:-1]
        count += 1
    # 1도 아니고 짝수도 아닌 홀수이면서 A로 나눠지지 않는 수는 만들 수 없다.
    else:
        print(-1)
        break
