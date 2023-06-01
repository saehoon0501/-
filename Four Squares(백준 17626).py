import sys

def input():
    return sys.stdin.readline().rstrip()

nums = [0]*50_001

i = 1
while True:    
    square = i**2
    if square > len(nums):
        break
    nums[square] = 1
    i = i+1

n = 0
for i in range(1,50001):
    if nums[i] == 0:        
        k = 1
        min = nums[i-(k**2)]
        while k < n:
            k += 1
            if min > nums[i-(k**2)]:
                min = nums[i-(k**2)]
        nums[i] = min + 1
    else:
        n += 1

N = int(input())
print(nums[N])