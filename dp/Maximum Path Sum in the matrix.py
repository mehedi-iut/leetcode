matrix = [
    [1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]
]


# # recursive approach
# # TC --> 3^(m*n)
# # SC --> O(m)
# def getMaxPathSum(matrix):
#     m, n = len(matrix), len(matrix[0])
#     max_sum = float("-inf")
#     for j in range(n):
#         max_sum = max(max_sum, recurse(m-1, j, matrix))
    
#     return max_sum

# def recurse(i, j, matrix):
#     if j < 0 or j > len(matrix[0])-1:
#         return float("-inf")
    
#     if i == 0:
#         return matrix[0][j]
    
#     up = matrix[i][j] + recurse(i-1, j, matrix)
#     ld = matrix[i][j] + recurse(i-1, j-1, matrix)
#     rd = matrix[i][j] + recurse(i-1, j+1, matrix)

#     return max(up, ld, rd)

# # memoization approach
# # TC --> O(m*n)
# # SC --> O(m) + O(m*n)

# def getMaxPathSum(matrix):

#     #   Write your code here
#     m, n = len(matrix), len(matrix[0])
#     dp = [[-1]*n for _ in range(m)]
#     max_sum = float("-inf")
#     for j in range(n):
#         max_sum = max(max_sum, recurse(m-1, j, matrix, dp))
#     return max_sum

# def recurse(i, j, matrix, dp):
#     if j > len(matrix[0])-1 or j < 0:
#         return float("-inf")
    
#     if i == 0:
#         return matrix[0][j]
    
#     if dp[i][j] != -1:
#         return dp[i][j]
    
#     up = matrix[i][j] + recurse(i-1, j, matrix, dp)
#     ld = matrix[i][j] + recurse(i-1, j-1, matrix, dp)
#     rd = matrix[i][j] + recurse(i-1, j+1, matrix, dp)
#     dp[i][j] = max(up, ld, rd)
#     return dp[i][j]


# # Tabulation approach

# def getMaxPathSum(matrix):
#     m, n = len(matrix), len(matrix[0])
#     dp = [[-1]*n for _ in range(m)]
#     for j in range(n):
#         dp[0][j] = matrix[0][j]
    

#     for i in range(1, m):
#         for j in range(n):
#             up = matrix[i][j] + dp[i-1][j]
#             if j-1 >= 0:
#                 ld = matrix[i][j] + dp[i-1][j-1]
#             else:
#                 ld = float("-inf")
#             if j+1 < n:
#                 rd = matrix[i][j] + dp[i-1][j+1]
#             else:
#                 rd = float("-inf")
#             dp[i][j] = max(up, ld, rd)

#     max_sum = float("-inf")
#     for j in range(n):
#         max_sum = max(max_sum, dp[m-1][j])
#     return max_sum

# space optimized

def getMaxPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    prev, curr = [0]*n, [0]*n
    for j in range(n):
        prev[j] = matrix[0][j]
    

    for i in range(1, m):
        for j in range(n):
            up = matrix[i][j] + prev[j]
            ld = matrix[i][j]
            if j-1 >= 0:
                ld += prev[j-1]
            else:
                ld += float("-inf")
            rd = matrix[i][j]
            if j+1 < n:
                rd += prev[j+1]
            else:
                rd += float("-inf")
            
            curr[j] = max(up, ld, rd)

        prev = curr
        curr = [0]*n

    max_sum = float("-inf")
    for j in range(n):
        max_sum = max(max_sum, prev[j])
    return max_sum


res = getMaxPathSum(matrix)
print(res)