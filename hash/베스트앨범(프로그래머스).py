def solution(genres, plays):
    genreCount = {g: 0 for g in genres}
    playCount = {g: [] for g in genres}
    answer = []
    for i in range(len(genres)):
        genreCount[genres[i]] += plays[i]
        playCount[genres[i]].append([i, plays[i]])

    tmp = []

    for item in genreCount.items():
        tmp.append(item)
    tmp.sort(key=lambda x: (-x[1]))

    for genre, count in tmp:
        playCount[genre].sort(key=lambda x: (-x[1]))
        for i in range(min(2, len(playCount[genre]))):
            answer.append(playCount[genre][i][0])

    return answer
