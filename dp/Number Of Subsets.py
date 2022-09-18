num = [1, 2, 2, 3]
target = 3

n = len(num)
# recursion    
# def recurse(ind, sum):
#     if sum == 0: return 1
#     if ind == 0: return int(sum == num[0])
    
#     not_take = recurse(ind-1, sum)
    
#     take = 0
    
#     if num[ind] <= sum:
#         take = recurse(ind-1, sum - num[ind])
    
#     return take + not_take


# res = recurse(n-1, target)
# print(res)


## memoization
# dp = [[-1]*(target+1) for _ in range(n)]

# def recurse_memo(ind, sum_):
#     if sum_ == 0: return 1
#     if ind == 0: return int(sum_ == num[0])

#     if dp[ind][sum_] != -1:
#         return dp[ind][sum_]
    
#     not_take = recurse_memo(ind-1, sum_)
    
#     take = 0
    
#     if num[ind] <= sum_:
#         take = recurse_memo(ind-1, sum_ - num[ind])
    
#     dp[ind][sum_] = take + not_take
#     return dp[ind][sum_]

# res = recurse_memo(n-1, target)
# print(res)


## Tabulation
dp = [[0]*(target+1) for _ in range(n)]

# first base case, target == 0 
for i in range(n):
    dp[i][0] = 1

# second base case, target == arr[0]
if num[0] <= target:
    dp[0][num[0]] = 1

for ind in range(1, n):
    for tar in range(1, target+1):
        not_take = dp[ind-1][tar]
        take = 0
        if num[ind] <= tar:
            take = dp[ind-1][tar - num[ind]]
        
        dp[ind][tar] = take + not_take

print(dp[n-1][target])
