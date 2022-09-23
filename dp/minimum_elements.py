arr = [1,2,3]
target = 7

n = len(arr)
## recursion
# def recurse(ind, tar):
#     if ind == 0:
#         if tar % arr[0] == 0:
#             return tar // arr[0]
#         else:
#             return float('inf')
    
#     not_take = 0 + recurse(ind-1, tar)
#     take = float('inf')
#     if arr[ind] <= tar:
#         take = 1 + recurse(ind, tar - arr[ind])
    
#     return min(take, not_take)

## memoization
# dp = [[-1]*(target+1) for _ in range(n)]
# def recurse(ind, tar):
#     if ind == 0:
#         if tar % arr[0] == 0:
#             return tar // arr[0]
#         else:
#             return float("inf")
    
#     if dp[ind][tar] != -1:
#         return dp[ind][tar]
    
#     not_take = 0 + recurse(ind-1, tar)

#     take = float('inf')

#     if arr[ind] <= tar:
#         take = 1 + recurse(ind, tar - arr[ind])
    
#     dp[ind][tar] = min(take, not_take)

#     return dp[ind][tar]

# ans = recurse(n-1, target)

# if ans == float('inf'):
#     print(-1)
# else:
#     print(ans)


## tabulation
dp = [[0]*(target+1) for _ in range(n)]

for i in range(target+1):
    if i % arr[0] == 0:
        dp[0][i] = i // arr[0]
    else:
        dp[0][i] = float('inf')

for ind in range(1, n):
    for tar in range(target+1):
        not_take = 0 + dp[ind-1][tar]

        take = float('inf')

        if arr[ind] <= tar:
            take = 1 + dp[ind][tar - arr[ind]]
        
        dp[ind][tar] = min(not_take, take)

ans = dp[n-1][target]
if ans == float('inf'):
    ans = -1
print(ans) 