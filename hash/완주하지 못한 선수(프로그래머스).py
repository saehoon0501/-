def solution(participant, completion):
    hashC = {}
    hashP = {}
    answer = ""

    for c in completion:
        if hashC.__contains__(c):
            hashC[c] += 1
        else:
            hashC[c] = 1

    for p in participant:
        if hashP.__contains__(p):
            hashP[p] += 1
        else:
            hashP[p] = 1

    for key in hashP.keys():
        if not hashC.__contains__(key):
            answer = key
            break
        else:
            if hashP[key] != hashC[key]:
                answer = key
                break
    return answer
