# points = [[1,2,5], [3,1,1], [3,3,3]]
points = [
[10, 40, 70],
[20, 50, 80],
[30, 60, 90]
]

n = len(points)
c = len(points[0])
# recursive

def recurse(day, last_task):
	if day == 0:
		max_point = 0
		for i in range(len(points[day])):
			if i != last_task:
				max_point = max(max_point, points[day][i])
		return max_point

	maxi_point = 0
	for i in range(len(points[day])):
		
		if i != last_task:
			pts = points[day][i] + recurse(day-1, i)

			maxi_point = max(pts, maxi_point)

	return maxi_point

print(recurse(n-1, 3))

# memoization
# TC --> O(Nx4x3)
# SC --> O(N) + O(Nx4)
dp = [[-1]*(c+1) for _ in range(n+1)]

# def recurse(day, last_task):
#     if day == 0:
#         max_pts = 0
#         for i in range(len(points[0])):
#             if i != last_task:
#                 max_pts = max(max_pts, points[day][i])
#         return max_pts
    
#     if dp[day][last_task] != -1:
#         return dp[day][last_task]
    
#     max_pts = 0
#     for i in range(len(points[day])):
#         if i != last_task:
#             pts = points[day][i] + recurse(day-1, i)
#             max_pts = max(max_pts, pts)
    
#     dp[day][last_task] = max_pts
#     return dp[day][last_task]

# print(recurse(n-1, 3))



# tabulation
# TC --> O(nx4x3)
# SC --> O(nx4)
dp[0][0] = max(points[0][1], points[0][2])
dp[0][1] = max(points[0][0], points[0][2])
dp[0][2] = max(points[0][0], points[0][1])
dp[0][3] = max(points[0][0], points[0][1], points[0][2])

for i in range(1, n):
    for task in range(len(points[0])+1):
        dp[i][task] = 0
        for t in range(3):
            if t != task:
                pts = points[i][t] + dp[i-1][t]
                dp[i][task] = max(pts, dp[i][task])

print(dp[n-1][3])

# space optimize
# TC --> O(Nx4x3)
# SC --> O(4)
prev = [-1]*(c+1)
prev[0] = max(points[0][1], points[0][2])
prev[1] = max(points[0][0], points[0][2])
prev[2] = max(points[0][0], points[0][1])
prev[3] = max(points[0][0], points[0][1], points[0][2])


for day in range(1, n):
    temp = [0]*(c+1)
    for last in range(len(points[0])+1):
        temp[last] = 0
        for task in range(3):
            if task != last:
                pts = points[day][task] + prev[task]
                temp[last] = max(pts, temp[last])
    
    prev = temp

print(prev[c])