from typing import List
arr = [5, 2, 6, 4]
d = 3

## memoization
# def countPartitions(n: int, d: int, arr: List[int]) -> int:
#     # write your code here
#     total = sum(arr)
    
#     if total-d < 0:
#         return 0
#     if (total-d)%2 == 1:
#         return 0
    
#     target = (total - d)//2

#     dp = [[-1]*(target+1) for _ in range(n)]

#     def recurse(ind, target):
#         if ind == 0:
#             if target == 0 and arr[0] == 0: return 2
#             if target == 0 or target == arr[0]: return 1
#             return 0

#         if dp[ind][target] != -1:
#             return dp[ind][target]

#         not_take = recurse(ind-1, target)

#         take = 0
#         if arr[ind] <= target:
#             take = recurse(ind-1, target - arr[ind])

#         dp[ind][target] = (take + not_take) % (10**9+7)
#         return dp[ind][target]
#     return recurse(n-1, target)



## tabulation
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total = sum(arr)
    
    if total-d < 0:
        return 0
    if (total-d)%2 == 1:
        return 0
    
    target = (total - d)//2

    dp = [[0]*(target+1) for _ in range(n)]

    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
    
    if arr[0] !=0 and arr[0] <= target:
        dp[0][arr[0]] = 1
    
    for ind in range(1, n):
        for tar in range(1, target):
            not_take = dp[ind-1][tar]

            take = 0
            if arr[ind] <= tar:
                take = dp[ind-1][tar - arr[ind]]

            dp[ind][tar] = (take + not_take) % (10**9+7)
    return dp[n-1][tar]


print(countPartitions(len(arr), d, arr))