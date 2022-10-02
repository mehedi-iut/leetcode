amount = 5
coins = [1,2,5]

n = len(coins)
# dp = [[-1]*(amount+1) for _ in range(n)]
# ## recursion with memoization
# ## TC--> NXT
# ## SC--> NXT + Auxiliary space (we can't write O(n) as we can take same value as much as possible)
# def recursion(ind, target):
#     if ind == 0:
#         if target % coins[0] == 0:
#             return 1
#         else:
#             return 0
    
#     if dp[ind][target] != -1:
#         return dp[ind][target]
    
#     not_take = recursion(ind-1, target)
#     take = 0

#     if coins[ind] <= target:
#         take = recursion(ind, target - coins[ind])
    
#     dp[ind][target] = take + not_take

#     return dp[ind][target]

# print(recursion(n-1, amount))

## Tabulation
dp = [[0]*(amount+1) for _ in range(n)]
for t in range(amount+1):
    if t % coins[0] == 0:
        dp[0][t] = 1

for index in range(1,n):
    for t in range(amount+1):
        not_take = dp[index-1][t]
        take = 0

        if coins[index] <= t:
            take = dp[index][t - coins[index]]
        
        dp[index][t] = take + not_take

print(dp[n-1][amount])