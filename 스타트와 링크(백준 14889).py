import copy;

n = int(input());
scoreBoard = [list(map(int, input().split(" "))) for _ in range(n)];
team = [];
global minimum;
minimum = -1;

def dfs(scoreBoard, team, n):
    if len(team) == (n//2):
        global minimum;
        ret = getScoreGap(team, scoreBoard);
        if ret < minimum or minimum == -1:
            minimum = ret;        
        return;

    if len(team) == 0:
        for i in range((n//2)+1):
            team.append(i);
            dfs(scoreBoard, copy.deepcopy(team), n);
            team.pop();
    else:
        for i in range(team[len(team)-1]+1,n):
            team.append(i);
            dfs(scoreBoard, copy.deepcopy(team), n);
            team.pop();
    return;

def getScoreGap(team, scoreBoard):
    sumA = 0;
    sumB = 0;

    notTeam = [];

    for i in range(len(scoreBoard)):
        if i in team:
            continue;
        notTeam.append(i);

    for i in range(len(team)):
        for j in range(i,len(team)):
            sumA += scoreBoard[team[i]][team[j]] + scoreBoard[team[j]][team[i]];
            sumB += scoreBoard[notTeam[i]][notTeam[j]] + scoreBoard[notTeam[j]][notTeam[i]]

    return abs(sumA-sumB);

dfs(scoreBoard, team, n);
print(minimum);