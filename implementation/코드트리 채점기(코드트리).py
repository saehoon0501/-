import sys
from collections import defaultdict
import heapq

INF = sys.maxsize
input = sys.stdin.readline

# 도메인을 hash로 PQ를 모아놓음
waitQ = defaultdict(list)
# 현재 waitQ에 있는 url들
urlAtWaitQ = set()
# 우선순위에 따라 machine 가져오는 PQ
machineList = []
# (채점 시작 시간, 채점 domain) 정보를 채점기 별로 가짐
machineStatus = []
# waitQ에 들어있는 task 수 관리
global size
size = 0
# 현재 채점 진행 중 domain
stringLock = defaultdict(int)


def parseUrl(url):
    result = url.split("/")
    return result[0]


# 대기 큐에 task 추가
def pushQ(time, priority, url):
    global size

    if url in urlAtWaitQ:
        return
    # 대기 큐 크기 증가
    size += 1
    # 대기 큐에 해당하는 도메인의 pq에 task 최종적으로 추가
    domain = parseUrl(url)
    # 대기 큐에 있는 url 추가
    urlAtWaitQ.add(url)
    heapq.heappush(waitQ[domain], (priority, time, url))
    return


# 대기 큐에 있는 task 중 가장 우선순위가 높은 task를 가져옴
def popQ(domain):
    global size
    size -= 1
    _, _, url = heapq.heappop(waitQ[domain])
    urlAtWaitQ.remove(url)
    return


# N크기 만큼 채점기 초기화 및 초기 문제 요청 처리
def init(cmd):
    global machineList, machineStatus
    N, url = int(cmd[1]), cmd[2]
    machineList = [i for i in range(1, N + 1)]
    machineStatus = [None for _ in range(N + 1)]
    pushQ(1, 0, url)
    return


def attempting(t):
    if not machineList:
        return

    bestPriority, bestDomain, bestTime = INF, "", 0
    for domain, queue in waitQ.items():
        if not queue:
            continue
        if stringLock[domain] > t:
            continue
        if queue[0][0] < bestPriority or (
            queue[0][0] == bestPriority and queue[0][1] < bestTime
        ):
            bestPriority = queue[0][0]
            bestDomain = domain
            bestTime = queue[0][1]

    if bestPriority == INF:
        return

    machineIdx = heapq.heappop(machineList)
    machineStatus[machineIdx] = (t, bestDomain)
    popQ(bestDomain)
    stringLock[bestDomain] = INF
    return


def finish(cmd):
    time, idx = int(cmd[1]), int(cmd[2])
    if machineStatus[idx] == None:
        return
    startTime, domain = machineStatus[idx]
    gap = time - startTime
    stringLock[domain] = startTime + 3 * gap
    machineStatus[idx] = None
    heapq.heappush(machineList, idx)
    return


results = []


def checkSize():
    global size
    results.append(size)
    return


Q = int(input().rstrip())
for _ in range(Q):
    cmd = input().rstrip().split()

    if cmd[0] == "100":
        init(cmd)
    elif cmd[0] == "200":
        time, priority, url = int(cmd[1]), int(cmd[2]), cmd[3]
        pushQ(time, priority, url)
    elif cmd[0] == "300":
        attempting(int(cmd[1]))
    elif cmd[0] == "400":
        finish(cmd)
    else:
        checkSize()

for r in results:
    print(r)
