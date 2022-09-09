# Frog Jump 2

n = 5
k = 3
h = [10, 30, 40, 50, 20]

dp = [-1]*(n+1)

# def recurse(n):
# 	if n == 0: return 0
# 	if dp[n] != -1: return dp[n]

# 	min_steps = float("inf")

# 	for i in range(1, k+1):
# 		if n-i >= 0:
# 			steps = recurse(n-i) + abs(h[n] - h[n-i])
# 			min_steps = min(min_steps, steps)
# 	dp[n] = min_steps
# 	return dp[n]

# print(recurse(n-1))

dp[0] = 0
for i in range(1, n):

	min_steps = float("inf")
	for j in range(1, k+1):
		if i-j >=0:
			steps = dp[i-j] + abs(h[i] - h[i-j])
			min_steps = min(min_steps, steps)
	dp[i] = min_steps

print(dp[n-1])
