def solution(nums):
    answer = 0
    hash = {}
    count = 0

    for n in nums:
        if not hash.__contains__(n):
            count += 1
            hash[n] = 1

    if count >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = count
    return answer
