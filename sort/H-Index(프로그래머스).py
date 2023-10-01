def solution(citations):
    citations.sort()
    answer = 0

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            break

    return answer


# 문제에서 제시한 h번 이상 인용된 논문이 h편 이상일 경우 h-index라는 정의를 정확히 이해하지 못함
# 테스트 케이스 작성은 무조건 필수!!
