matrix = [[2,1,3],[6,5,4],[7,8,9]]
# matrix = [[-19,57],[-40,-5]]

m, n = len(matrix), len(matrix[0])


# def dp(r, c, matrix):
#     if r <0 or c < 0:
#         return float("inf")
#     if r >= m or c >= n:
#         return float("inf")
    
#     if r == 0:
#         return matrix[r][c]
    
#     up_l = matrix[r][c] + dp(r-1, c-1, matrix)
#     up_m = matrix[r][c] + dp(r-1, c, matrix)
#     up_r = matrix[r][c] + dp(r-1, c+1, matrix)
#     return min(up_l, up_m, up_r)
# ans = []
# for j in range(n):
#     ans.append(dp(m-1, j, matrix))

# # res = dp(m-1,n-1, matrix)
# print(min(ans))


# memoization
# memo = [[-1 for _ in range(n)] for _ in range(m)]

# def dp(r, c, matrix):
#     if r <0 or c < 0:
#         return float("inf")
#     if r >= m or c >= n:
#         return float("inf")
    
#     if memo[r][c] != -1:
#         return memo[r][c]
    
#     if r == 0:
#         return matrix[r][c]
    
#     up_l = matrix[r][c] + dp(r-1, c-1, matrix)
#     up_m = matrix[r][c] + dp(r-1, c, matrix)
#     up_r = matrix[r][c] + dp(r-1, c+1, matrix)
#     memo[r][c] = min(up_l, up_m, up_r)
#     return memo[r][c]

# ans = []
# for j in range(n):
#     ans.append(dp(m-1, j, matrix))

# print(min(ans))

# Tabulation
memo = [[-1 for _ in range(n)] for _ in range(m)]

memo[0][:] = matrix[0][:]

for i in range(1, m):
    for j in range(n):
        if j==0:
            memo[i][j] = matrix[i][j] + min(memo[i-1][j], memo[i-1][j+1])
        elif j == n-1:
            memo[i][j] = matrix[i][j] + min(memo[i-1][j-1], memo[i-1][j])
        else:
            memo[i][j] = matrix[i][j] + min(memo[i-1][j-1], memo[i-1][j], memo[i-1][j+1])


print(min(memo[-1][:]))