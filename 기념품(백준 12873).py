N = int(input())#게임을 플레이하는 인원
ppl = [i for i in range(N)]

pointing = 0
t = 1
while len(ppl) != 1:#게임에서 한명이 남을 때까지 반복하여 진행한다.    
    pointing = (t**3+pointing-1) % len(ppl)
    ppl.pop(pointing)
    t += 1

print(ppl[0]+1)