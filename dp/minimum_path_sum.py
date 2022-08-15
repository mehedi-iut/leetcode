grid = [[1,3,1],[1,5,1],[4,2,1]]
# output = 7

# class Solution:
#     def minPathSum(self, grid):
class Solution:
    def min_path_sum(self, grid):
        m, n = len(grid), len(grid[0])
        mem = [[-1 for _ in range(n)] for _ in range(m)]
        def recurse(r, c, res):
            if r < 0 or c < 0:
                return float("inf")
            if r == 0 and c == 0:
                return grid[r][c]
            if mem[r][c] != -1:
                return mem[r][c]
            
            up = grid[r][c] + recurse(r-1, c, res)
            left = grid[r][c] + recurse(r, c-1, res)
            mem[r][c] = min(up, left)
            
            return mem[r][c]
        return recurse(2,2, grid)

sln = Solution()
output = sln.min_path_sum(grid)
print(output)