N = int(input())


def dfs(arr):
    # 배열에서 가장 최근에 들어온 수의 마지막 자리 값을 가져와 이보다 작은 숫자만을 붙인다.
    # 이를 반복한다.
    last = str(arr[-1])
    for i in range(int(last[-1])):
        newNum = "".join([last, str(i)])
        arr.append(int(newNum))
        dfs(arr)


arr = []
for i in range(10):
    arr.append(i)
    dfs(arr)

# 줄어드는 수들을 만들었지만 크기 순으로 정렬되지 않았기에 오름차순으로 정렬한다.
arr.sort()

if N > len(arr):
    print(-1)
else:
    print(arr[N - 1])
