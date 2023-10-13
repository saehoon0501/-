import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

Q = int(input())
INF = sys.maxsize
machineList = []
machineOnWorked = []
size = 0
urlAtWaitQ = set()
waitQ = defaultdict(list)
stringLock = defaultdict(int)


# 채점기 수에 맞춰 관련 자료구조 초기화
def init(N):
    global machineList, machineOnWorked
    machineList = [i for i in range(1, N + 1)]
    machineOnWorked = [None for _ in range(N + 1)]


def parseUrl(url):
    return url.split("/")[0]


def pushQ(time, priority, url):
    global size
    # 대기큐에 이미 일치 url이 존재하면 패스
    if url in urlAtWaitQ:
        return
    size += 1
    urlAtWaitQ.add(url)
    heapq.heappush(waitQ[parseUrl(url)], (priority, time, url))


def attempting(time):
    global size
    # 쉬고 있는 채점기가 없다면 패스
    if not machineList:
        return
    # waitQ에서 우선순위가 가장 높은 것을 비교해 가져온다.
    # task 중 채점될 수 없는 조건을 확인해 그 task는 비교하지 않는다.
    bestPriority, bestTime, bestDomain = INF, INF, ""
    for domain, queue in waitQ.items():
        if not queue:
            continue
        if stringLock[domain] > time:
            continue
        if queue[0][0] < bestPriority or (
            queue[0][0] == bestPriority and queue[0][1] < bestTime
        ):
            bestPriority, bestTime = queue[0][0], queue[0][1]
            bestDomain = domain

    if bestPriority == INF:
        return

    _, _, bestUrl = heapq.heappop(waitQ[bestDomain])
    urlAtWaitQ.remove(bestUrl)
    size -= 1
    machine = heapq.heappop(machineList)
    machineOnWorked[machine] = (time, bestUrl)
    stringLock[bestDomain] = INF


def finish(time, J_id):
    if machineOnWorked[J_id] == None:
        return
    start, url = machineOnWorked[J_id]
    gap = time - start
    stringLock[parseUrl(url)] = start + 3 * gap
    machineOnWorked[J_id] = None
    heapq.heappush(machineList, J_id)


results = []
for _ in range(Q):
    cmd = input().rstrip().split()

    if cmd[0] == "100":
        init(int(cmd[1]))
        pushQ(0, 1, cmd[2])
    elif cmd[0] == "200":
        pushQ(int(cmd[1]), int(cmd[2]), cmd[3])
    elif cmd[0] == "300":
        attempting(int(cmd[1]))
    elif cmd[0] == "400":
        finish(int(cmd[1]), int(cmd[2]))
    else:
        results.append(size)
for r in results:
    print(r)
