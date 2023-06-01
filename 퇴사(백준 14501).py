
n = int(input());
plan = [list(map(int, input().split(" "))) for _ in range(n)];
dp = [0]*(n+1);

def maximumProfit(plan, dp):

    for i in range(len(plan)):
        for j in range(i+plan[i][0], len(plan)+1):
            if dp[j] < dp[i] + plan[i][1]:
                dp[j] = dp[i] + plan[i][1];
    
    return dp[-1];

result = maximumProfit(plan, dp);
print(result);