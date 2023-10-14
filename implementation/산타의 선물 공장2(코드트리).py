import sys

input = sys.stdin.readline
results = []


class Node:
    def __init__(self, p_num):
        self.prev = None
        self.next = None
        self.p_num = p_num

    def setNext(self, node):
        self.next = node
        return

    def setPrev(self, node):
        self.prev = node
        return

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def __repr__(self) -> str:
        return f"{self.p_num}"


class DoubleLinkedList:
    def __init__(self, b_num):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)
        self.b_num = b_num
        self.size = 0

    def append(self, node):
        lastNode = self.tail.getPrev()
        lastNode.setNext(node)
        node.setPrev(lastNode)
        self.tail.setPrev(node)
        node.setNext(self.tail)
        self.size += 1

    def getTop(self):
        return self.head.getNext()

    def getLast(self):
        return self.tail.getPrev()

    def __repr__(self) -> str:
        node = self.head
        result = ""
        while node != None and node.p_num != 0:
            result += str(node.p_num) + " "
            node = node.getNext()

        if node == None:
            result += f"size{self.size}" + "\n"
            return result
        result += f"size{self.size}" + "\n"
        return result


def init(N, M, sequence):
    global conveyBelt, presents
    conveyBelt = [DoubleLinkedList(i) for i in range(N + 1)]
    presents = []

    for i in range(len(sequence)):
        b_num = sequence[i]
        present = Node(i + 1)
        conveyBelt[b_num].append(present)
        presents.append(present)
    return


def moveAll(m_src, m_dst):
    srcBelt = conveyBelt[m_src]
    dstBelt = conveyBelt[m_dst]

    if srcBelt.size == 0:
        results.append(dstBelt.size)
        return

    srcTop = srcBelt.getTop()
    srcLast = srcBelt.getLast()

    srcBelt.head.setNext(srcBelt.tail)
    srcBelt.tail.setPrev(srcBelt.head)

    dstTop = dstBelt.getTop()
    srcLast.setNext(dstTop)
    dstTop.setPrev(srcLast)
    srcTop.setPrev(dstBelt.head)
    dstBelt.head.setNext(srcTop)

    dstBelt.size += srcBelt.size
    srcBelt.size = 0
    results.append(dstBelt.size)
    return


def addNodeSrctoEmpty(srcBelt, dstBelt):
    srcTop = srcBelt.getTop()

    srcSecond = srcTop.getNext()
    srcBelt.head.setNext(srcSecond)
    srcSecond.setPrev(srcBelt.head)

    srcTop.setPrev(dstBelt.head)
    dstBelt.head.setNext(srcTop)
    srcTop.setNext(dstBelt.tail)
    dstBelt.tail.setPrev(srcTop)

    dstBelt.size += 1
    srcBelt.size -= 1

    return


def swithNode(srcBelt, dstBelt):
    srcTop = srcBelt.getTop()
    dstTop = dstBelt.getTop()
    srcSecond = srcTop.getNext()
    dstSecond = dstTop.getNext()

    dstTop.setPrev(srcBelt.head)
    srcBelt.head.setNext(dstTop)
    srcTop.setPrev(dstBelt.head)
    dstBelt.head.setNext(srcTop)

    dstTop.setNext(srcSecond)
    srcSecond.setPrev(dstTop)
    srcTop.setNext(dstSecond)
    dstSecond.setPrev(srcTop)


# 서로 앞 물건만 교체하기
def moveOnlyFront(m_src, m_dst):
    srcBelt = conveyBelt[m_src]
    dstBelt = conveyBelt[m_dst]

    if srcBelt.size == 0 and dstBelt.size == 0:
        results.append(dstBelt.size)
        return
    elif srcBelt.size == 0:
        addNodeSrctoEmpty(dstBelt, srcBelt)
    elif dstBelt.size == 0:
        addNodeSrctoEmpty(srcBelt, dstBelt)
    else:
        swithNode(srcBelt, dstBelt)

    results.append(dstBelt.size)
    return


def splitInHalf(m_src, m_dst):
    srcBelt = conveyBelt[m_src]
    dstBelt = conveyBelt[m_dst]

    if srcBelt.size <= 1:
        results.append(dstBelt.size)
        return
    nth = srcBelt.size // 2
    srcTop = srcBelt.getTop()
    nth_src = srcTop
    count = 1
    while count < nth:
        nth_src = nth_src.getNext()
        count += 1
    nthNext = nth_src.getNext()
    srcBelt.head.setNext(nthNext)
    nthNext.setPrev(srcBelt.head)

    dstTop = dstBelt.getTop()
    dstTop.setPrev(nth_src)
    nth_src.setNext(dstTop)
    dstBelt.head.setNext(srcTop)
    srcTop.setPrev(dstBelt.head)

    srcBelt.size -= nth
    dstBelt.size += nth

    results.append(dstBelt.size)
    return


def getPresent(p_num):
    a, b = 0, 0
    present = presents[p_num - 1]
    prev = present.getPrev()
    next = present.getNext()

    if prev.p_num == -1:
        a = -1
    else:
        a = prev.p_num
    if next.p_num == 0:
        b = -1
    else:
        b = next.p_num
    results.append(a + 2 * b)


def getBelt(b_num):
    a, b, c = 0, 0, 0
    belt = conveyBelt[b_num]
    top = belt.getTop()
    last = belt.getLast()

    if belt.size == 0:
        a, b = -1, -1
    else:
        a = top.p_num
        b = last.p_num

    c = belt.size
    results.append(a + 2 * b + 3 * c)
    return


Q = int(input().rstrip())
conveyBelt = []
presents = []
results = []
for _ in range(Q):
    cmd = input().rstrip().split()

    if cmd[0] == "100":
        init(int(cmd[1]), int(cmd[2]), list(map(int, cmd[3:])))
    elif cmd[0] == "200":
        moveAll(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "300":
        moveOnlyFront(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "400":
        splitInHalf(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "500":
        getPresent(int(cmd[1]))
    else:
        getBelt(int(cmd[1]))
for r in results:
    print(r)
