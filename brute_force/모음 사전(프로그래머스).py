def solution(word):
    answer = 0
    global results
    results = []
    created = set()
    dfs("", word, 0, created)

    for idx in range(len(results)):
        if results[idx] == word:
            answer = idx + 1
    return answer


def dfs(letter, word, count, created):
    global results
    if count != 0:
        if letter not in created:
            results.append(letter)
            created.add(letter)

    if count == 5:
        return

    for alphabet in ["A", "E", "I", "O", "U"]:
        dfs("".join([letter, alphabet]), word, count + 1, created)

    return
