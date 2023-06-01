N,M = map(int, input().split(" "))
nums = [[0]*101 for _ in range(101)]

nums[0][0] = 1

for num in range(1,101):
    nums[num][0] = 1
    for select in range(1,101):
        nums[num][select] = nums[num-1][select] + nums[num-1][select-1]

print(nums[N][M])
