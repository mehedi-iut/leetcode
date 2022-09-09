# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

# matrix = [["1","0","0"], ["1","1","1"], ["0","1","1"]]

# matrix = [["0","1"],["1","0"]]
matrix = [["1"]]
m = len(matrix)
n = len(matrix[0])

# mat = [list(map(int,matrix[i])) for i in range(m)]

# ans = 0

# for i in range(m):
# 	for j in range(n):

# 		if mat[i][j] == 1:

# 			if i == 0 or j == 0:
# 				ans = max(ans, 1)
# 				continue

# 			else:
# 				mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
# 				ans = max(ans, mat[i][j])

# print(ans**2)

# memo = [[-1 for _ in range(n)] for _ in range(m)]

# def dp(mat, i, j, ans):
# 	if i >= m or j >= n: return 0

# 	if mat[i][j] == 0:
# 		res = 0
# 	else:
# 		right = dp(mat, i, j+1, ans)
# 		down = dp(mat, i+1, j, ans)
# 		diag = dp(mat, i+1, j+1, ans)
# 		res = 1 + min(right, down, diag)

# 	ans = max(ans, res)
# 	print(ans)

# 	return res

# dp(mat, 0, 0, ans)
# print(ans)


# # recursion only
# class Solution:
# 	def maximalSquare(self, matrix):
# 		m = len(matrix)
# 		n = len(matrix[0])

# 		self.max_val = 0
# 		res = 0

# 		def recurse(r, c):
# 			if r < 0 or c < 0:
# 				return 0
			
# 			left = recurse(r, c-1)
# 			top = recurse(r-1, c)
# 			diag = recurse(r-1, c-1)
# 			res = 0
# 			if matrix[r][c] != "0":
# 				res = 1 + min(top, left, diag)

# 			self.max_val = max(res, self.max_val)

# 			return res
		
# 		recurse(m-1, n-1)
# 		return self.max_val


# # memoization
# memo = [[-1 for _ in range(n)] for _ in range(m)]

# class Solution:
# 	def maximalSquare(self, matrix):
# 		m = len(matrix)
# 		n = len(matrix[0])

# 		self.max_val = 0
# 		res = 0

# 		def recurse(r, c):
# 			if r < 0 or c < 0:
# 				return 0
			
# 			if memo[r][c] != -1:
# 				return memo[r][c]
			
# 			left = recurse(r, c-1)
# 			top = recurse(r-1, c)
# 			diag = recurse(r-1, c-1)
# 			res = 0
# 			if matrix[r][c] != "0":
# 				res = 1 + min(top, left, diag)
# 				memo[r][c] = res

# 			self.max_val = max(res, self.max_val)

# 			return memo[r][c]
		
# 		recurse(m-1, n-1)
# 		return self.max_val

# Tabulation method
# TC = O(m*n)
# SC = O(m*n)

class Solution:
	def maximalSquare(self, matrix):
		m, n = len(matrix), len(matrix[0])
		memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
		ans = 0
		for i in range(1, m+1):
			for j in range(1, n+1):
				
				if matrix[i-1][j-1] == "1":
					memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
					ans = max(ans, memo[i][j])

		return ans

sln = Solution()
res = sln.maximalSquare(matrix)

print(res*res)


