def solution(phone_book):
    hash = {number: 0 for number in phone_book}

    for key in hash.keys():
        for i in range(len(key) - 1):
            if hash.__contains__(key[0 : i + 1]):
                answer = False
                return answer

    answer = True
    return answer
