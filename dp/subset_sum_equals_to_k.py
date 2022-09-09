arr = [2, 5, 1, 6, 7]
k = 4

## Recursive with memoization
# def subsetSumToK(n, k, arr):

#     # Write your code here
#     # Return a boolean variable 'True' or 'False' denoting the answer
#     dp = [[-1]*(k+1) for _ in range(n)]
#     def recurse(ind, target):
#         if target == 0: return True

#         if ind == 0: return arr[0] == target
    
#         if dp[ind][target] != -1:
#             return dp[ind][target]

#         not_take = recurse(ind-1, target)
#         take = False

#         if arr[ind] <= target:
#             take = recurse(ind-1, target-arr[ind])
#         dp[ind][target] = take or not_take
#         return dp[ind][target]
#     return recurse(n-1, k)

## tabulation
def subsetSumToK(n, k, arr):
    dp = [[False]*(k+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for ind in range(1, n):
        for target in range(1, k+1):
            not_take = dp[ind-1][target]
            take = False

            if arr[ind] <= target:
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target] = take or not_take
    return dp[n-1][k]
    
res = subsetSumToK(len(arr)-1, k, arr)
print(res)

