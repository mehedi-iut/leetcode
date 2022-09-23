nums = [1,1,1,1,1]
target = 3
# ans = 5

def find_ways(num, tar):
    n = len(num)

    dp = [[0]*(tar+1) for _ in range(n)]

    if num[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1
    
    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1
    
    for ind in range(1, n):
        for target in range(tar+1):
            not_taken = dp[ind-1][target]

            taken = 0

            if num[ind] <= target:
                taken = dp[ind-1][target - num[ind]]
            dp[ind][target] = not_taken + taken
    return dp[n-1][tar]


def target_sum(nums, target):
    total_sum = sum(nums)

    if total_sum - target < 0 or (total_sum -target)%2 == 1:
        return 0
    
    return find_ways(nums, (total_sum-target)//2)

print(target_sum(nums, target))