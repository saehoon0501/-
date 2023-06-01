nums = [0]*(10**6+1)
nums[1] = 0
INF = float('inf')

for i in range(2,10**6+1):
    a,b,c = INF,INF,INF
    if i % 3 == 0:
        a = nums[i//3]
    if i % 2 == 0:
        b = nums[i//2]
    c = nums[i-1]

    nums[i] = min(a,b,c) + 1

N = int(input())
print(nums[N])