nums = [0]*10
nums[0] = 1
nums[1] = 2
nums[2] = 4

for i in range(3,10):
    nums[i] = nums[i-1] + nums[i-2] + nums[i-3]

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(nums[N-1])

for result in results:
    print(result)