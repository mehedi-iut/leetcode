N = 5
prices = [2,5,7,8,10]

n = len(prices)
dp = [[-1]*(N+1) for _ in range(n)]

def recursion(ind, target):
    if ind == 0:
        return target*prices[0]
    
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    not_take = 0 + recursion(ind-1, target)
    take = 0
    rod_length = ind + 1
    if rod_length <= target:
        take = prices[ind] + recursion(ind, target - rod_length)
    dp[ind][target] = max(take, not_take)
    return dp[ind][target]

print(recursion(n-1, N))


# tabulation
dp = [[0]*(N+1) for _ in range(n)]
# handle the base case
for i in range(N+1):
    dp[0][i] = i*prices[0]

for ind in range(1, n):
    for t in range(N+1):
        not_take = 0 + dp[ind-1][t]
        take = 0
        rod_length = ind + 1
        if rod_length <= t:
            take = prices[ind] + dp[ind][t - rod_length]
        dp[ind][t] = max(take, not_take)

print(dp[n-1][N])