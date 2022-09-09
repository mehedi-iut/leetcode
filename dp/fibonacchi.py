n = 7
# recursion to memoization
# step 1:
# declare the dp array with n+1 size with value -1
dp = [-1]*(n+1)

# def fibo(n):
# 	if n <= 1:
# 		return n
# 	# step:2
# 	if dp[n] != -1:
# 		return dp[n]

# 	return fibo(n-1) + fibo(n-2)
# res = fibo(n)
# tabulation
# step-1
# complete the base condition
# dp[0] = 0
# dp[1] = 1

# for i in range(2, n+1):
# 	dp[i] = dp[i-1] + dp[i-2]

# res = dp[n]


# space optimize tabulation
prev2 = 0
prev = 1

for i in range(2, n+1):
	curr = prev2 + prev
	prev2 = prev
	prev = curr

res = prev

print(res)