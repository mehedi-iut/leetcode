
arr = [1,2,3,4]

def minSubsetSumDifference(arr, n):
    # Write your code here.
    # Return the minimum difference in the form of an integer.
    total_sum = sum(arr)
    dp = [[False]*(total_sum+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    # if first element of the given arr is less or equal to total sum
    # arr[0] value will be taken and set True in dp matrix
    # if arr = [4,6,9,2]
    # here arr[0]= 4
    # so in dp[0][4] we will set True
    if arr[0] <= total_sum:
        dp[0][total_sum] = True
    
    for ind in range(1, n):
        for target in range(1, total_sum+1):
            not_take = dp[ind-1][target]
            take = False
            if arr[ind] <= target:
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target] = take or not_take

    print(dp)

    min_val = float("inf")

    for i in range(total_sum+1):
        if dp[n-1][i] == True:
            diff = abs(i - (total_sum - i))
            min_val = min(min_val, diff)
    return min_val


res = minSubsetSumDifference(arr, len(arr))
print(res)