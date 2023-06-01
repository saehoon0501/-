def getShortestTime(bananas, gorilla):
    totalTime = 0;# 최단시간
    distanceFromLeft = abs(bananas[0] - gorilla);#고릴라에서 가장 왼쪽에 위치한 바나나 위치
    distanceFromRight = abs(bananas[len(bananas)-1] - gorilla);#고릴라에서 가장 오른쪽에 위치한 바나나 위치
    distanceBetweenLeftNRight = abs(bananas[0]+bananas[len(bananas)-1]);

    if distanceFromLeft <= distanceFromRight:# 왼쪽 방향이 좀더 가깝거나 서로 방향이 같은 경우
        totalTime = distanceFromLeft + distanceBetweenLeftNRight; #결국 총 거리는 왼쪽 거리 두번 오른쪽 거리 한번이다.
    else: # 오른쪽 방향이 좀더 가까운 경우
        totalTime += distanceFromRight + distanceBetweenLeftNRight; #총 거리는 오른쪽 거리 두번 왼쪽 거리 한번이다.

    print(totalTime);

if __name__ == "__main__":
    gorilla = int(input()); # 고릴라 위치 값
    bananas = list(map(int, input().split(" "))); # 바나나 위치 값들 저장 배열

    bananas.sort(); # 바나나 위치 값들을 오름차순으로 정렬한다.

    getShortestTime(bananas, gorilla)# 고릴라가 바나나를 가지러 이동하는 최단시간을 구한다.
