def solution(clothes):
    hash = {}
    for name, item in clothes:
        if item not in hash:
            hash[item] = 1
        else:
            hash[item] += 1

    answer = 1

    for val in hash.values():
        answer *= val + 1

    return answer - 1
