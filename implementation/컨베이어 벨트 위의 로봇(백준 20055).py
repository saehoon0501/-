from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = deque()
global count
count = 0


def rotate():
    i = 0
    prev = belt[i]
    while True:
        if i == 2 * N - 1:
            belt[0] = prev
            break
        tmp = belt[i + 1]
        belt[i + 1] = prev
        prev = tmp
        i += 1

    for i in range(len(robot)):
        if robot[i] == N - 2:
            robot.pop()
            break
        robot[i] += 1
    return


def moveRobot(robot):
    global count
    result = deque()
    for i in range(len(robot) - 1, -1, -1):
        idx = robot[i]
        # 로봇이 N칸에 있으면 한 칸 이동 시 바로 내리기에 저장하지 않음
        if belt[idx + 1] > 0 and idx + 1 == N - 1:
            belt[idx + 1] -= 1
            if belt[idx + 1] == 0:
                count += 1
            continue
        # 로봇이 이동하려는 칸의 내구도와 로봇의 존재 유무 확인
        if belt[idx + 1] > 0 and idx + 1 not in result:
            result.appendleft(idx + 1)
            belt[idx + 1] -= 1
            if belt[idx + 1] == 0:
                count += 1
        else:
            result.appendleft(idx)
    return result


step = 1

while True:
    rotate()
    robot = moveRobot(robot)
    if belt[0] > 0:
        robot.appendleft(0)
        belt[0] -= 1
        if belt[0] == 0:
            count += 1
    if count >= K:
        break
    step += 1
print(step)
