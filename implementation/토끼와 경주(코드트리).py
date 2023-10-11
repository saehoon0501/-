import heapq


class Rabbit:
    def __init__(self, pid, dist):
        self.dist = dist
        self.pid = pid
        self.coord = (1, 1)
        self.jumped = 0
        self.score = 0

    def __repr__(self) -> str:
        return f"Rabbit {self.pid}, Coord {self.coord}, Jumped {self.jumped} Score{self.score}, Dist{self.dist}"

    def __lt__(self, other):
        if self.jumped < other.jumped:
            return True
        elif self.jumped == other.jumped:
            if self.coord[0] + self.coord[1] < other.coord[0] + other.coord[1]:
                return True
            elif self.coord[0] + self.coord[1] == other.coord[0] + other.coord[1]:
                if self.coord[0] < other.coord[0]:
                    return True
                elif self.coord[0] == other.coord[0]:
                    if self.pid < other.pid:
                        return True

        return False


class Slot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Slot X{self.x}, Y{self.y}"

    def __lt__(self, other):
        if self.x + self.y > other.x + other.y:
            return True
        elif self.x + self.y == other.x + other.y:
            if self.x > other.x:
                return True
        return False


Q = int(input())

cmd = list(map(int, input().split()))
N, M, P = cmd[1], cmd[2], cmd[3]
rabbits = []
global addup
addup = 0
hash = {}
for i in range(P):
    pid, d = cmd[4 + 2 * i], cmd[5 + 2 * i]
    rabbit = Rabbit(pid, d)
    rabbits.append(rabbit)
    hash[pid] = rabbit

hasJumped = {}
heapq.heapify(rabbits)


def moveDown(d, x):
    if N - x >= d:
        return 0, x + d
    else:
        return d - N + x, N


def moveUp(d, x):
    if x - 1 >= d:
        return 0, x - d
    else:
        return d - x + 1, 1


def moveRight(d, y):
    if M - y >= d:
        return 0, y + d
    else:
        return d - M + y, M


def moveLeft(d, y):
    if y - 1 >= d:
        return 0, y - d
    else:
        return d - y + 1, 1


def moveRabbit():
    global addup
    rabbit = heapq.heappop(rabbits)
    results = []
    # 아래,오른쪽,왼쪽,위 순으로 칸 이동 후 우선순위에 따라 (r,c)결정
    # 아래
    d = (rabbit.dist) % (2 * (N - 1))
    current = rabbit.coord

    d, currentX = moveDown(d, current[0])
    d, currentX = moveUp(d, currentX)
    d, currentX = moveDown(d, currentX)
    results.append(Slot(currentX, current[1]))

    # 오른쪽
    d = (rabbit.dist) % (2 * (M - 1))

    d, currentY = moveRight(d, current[1])
    d, currentY = moveLeft(d, currentY)
    d, currentY = moveRight(d, currentY)
    results.append(Slot(current[0], currentY))

    # 왼쪽
    d = (rabbit.dist) % (2 * (M - 1))

    d, currentY = moveLeft(d, current[1])
    d, currentY = moveRight(d, currentY)
    d, currentY = moveLeft(d, currentY)
    results.append(Slot(current[0], currentY))

    # 위쪽
    d = (rabbit.dist) % (2 * (N - 1))

    d, currentX = moveUp(d, current[0])
    d, currentX = moveDown(d, currentX)
    d, currentX = moveUp(d, currentX)
    results.append(Slot(currentX, current[1]))

    heapq.heapify(results)
    slot = heapq.heappop(results)
    rabbit.coord = (slot.x, slot.y)
    rabbit.jumped += 1
    if not hasJumped.__contains__(rabbit.pid):
        hasJumped[rabbit.pid] = rabbit
    addup += slot.x + slot.y
    rabbit.score -= slot.x + slot.y
    heapq.heappush(rabbits, rabbit)


def multiplyDist(pid, L):
    rabbit = hash[pid]
    rabbit.dist *= L
    return


def getWinner():
    pid, sum, maxX = 0, -1, -1
    for rabbit in hasJumped.values():
        if rabbit.coord[0] + rabbit.coord[1] > sum:
            pid, sum, maxX = (
                rabbit.pid,
                rabbit.coord[0] + rabbit.coord[1],
                rabbit.coord[0],
            )
        elif rabbit.coord[0] + rabbit.coord[1] == sum:
            if rabbit.coord[0] > maxX:
                pid, sum, maxX = (
                    rabbit.pid,
                    rabbit.coord[0] + rabbit.coord[1],
                    rabbit.coord[0],
                )
            elif rabbit.coord[0] == maxX:
                if rabbit.pid > pid:
                    pid, sum, maxX = (
                        rabbit.pid,
                        rabbit.coord[0] + rabbit.coord[1],
                        rabbit.coord[0],
                    )
    return pid


for _ in range(Q - 1):
    cmd = list(map(int, input().split()))

    if cmd[0] == 200:
        hasJumped = {}
        count = 0
        # K번 움직임
        while count < cmd[1]:
            moveRabbit()
            count += 1
        # 점수 S를 준다.
        rabbit = hash[getWinner()]
        rabbit.score += cmd[2]

    elif cmd[0] == 300:
        # 토끼 pid에 dist를 L만큼 곱한다.
        multiplyDist(cmd[1], cmd[2])
    else:
        result = 0
        # 최고의 토끼 선정
        for rabbit in rabbits:
            result = max(result, rabbit.score)
        print(result + addup)
