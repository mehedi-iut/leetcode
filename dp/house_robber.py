nums = [2,7,9,3,1]

n = len(nums)

# def recurse(n):
# 	if n == 0: return nums[n]
# 	if n < 0: return 0

# 	pick = recurse(n-2) + nums[n]
# 	not_pick = recurse(n-1) + 0

# 	return max(pick, not_pick)

# print(recurse(n-1))


dp = [-1]*n

# def recurse_mem(n):
# 	if n == 0: return nums[n]
# 	if n < 0: return 0
# 	if dp[n] != -1: return dp[n]

# 	pick = recurse_mem(n-2) + nums[n]
# 	not_pick = recurse_mem(n-1) + 0

# 	dp[n] = max(pick, not_pick)
# 	return dp[n]

# print(recurse_mem(n-1))

# tabulation method
dp[0] = nums[0]
        
for i in range(1, n):
    pick = nums[i]
    if i > 1:
        pick += dp[i-2]
    not_pick = dp[i-1] + 0
    
    dp[i] = max(pick, not_pick)

print(dp[n-1])



# space optimized
prev = nums[0]
prev2 = 0

for i in range(1, n):
	pick = nums[i] + prev2
	not_pick = 0 + prev
	curr = max(pick, not_pick)

	prev2 = prev
	prev = curr

print(prev)