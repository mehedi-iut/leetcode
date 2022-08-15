obstacleGrid = [[0,0,0], [0,1,0], [0,0,0]]

def dp(r, c, obstacleGrid):
    if r < 0 or c < 0:
        return 0
    if obstacleGrid[r][c] == 1:
        return 0
    if r == 0 and c== 0:
        return 1

    up = dp(r-1, c, obstacleGrid)
    left = dp(r, c-1, obstacleGrid)
    return up + left
m, n = len(obstacleGrid), len(obstacleGrid[0])
print(dp(m-1,n-1, obstacleGrid))

