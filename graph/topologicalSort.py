# prerequisites = [[3,1], [2,1], [2,3], [2,4]]
# # step:1
# # Create the Adjacency list
# adjacency_map = {}
# for data in prerequisite:
# 	if data[1] in adjacency_map:
# 		adjacency_map[data[1]].append(data[0])
# 	else:
# 		adjacency_map[data[1]] = [data[0]]

# print(adjacency_map)

# # Step:2
# # Create indegree map
# indegree_map = {}
# for data in prerequisite:
# 	if data[0] in indegree_map:
# 		indegree_map[data[0]] += 1
# 	else:
# 		indegree_map[data[0]] = 1

# print(indegree_map)

# # step:3
# # run DFS on adjacency list
# visited = set()
# def dfs(root):
# 	stack = [root]
# 	while stack:
# 		node = stack.pop()
# 		for child in adjacency_map[node]:
# 			if child not in visited:
# 				stack.append(child)
# 			else:
# 				# child in visited array, return false
# 				return False

# 		if indegree_map[node] == 0:
# 			visited.add(node)
# 		else:
# 			indegree_map[node] -= 1
# 	return visited

def canFinish(numCourses, prerequisites) -> bool:
        adjacency_map = {}
        for data in prerequisites:
            if data[1] in adjacency_map:
                adjacency_map[data[1]].append(data[0])
            else:
                adjacency_map[data[1]] = [data[0]]
        
        indegree_map = {}
        for data in prerequisites:
            if data[0] in indegree_map:
                indegree_map[data[0]] += 1
            else:
                indegree_map[data[0]] = 1
        
        visited = set()
        
        def dfs(root):
            stack = [root]
            while stack:
                node = stack.pop()
                if node in visited:
                    return False
                if node in adjacency_map:
                    for child in adjacency_map[node]:
                        stack.append(child)
        
                if node in indegree_map:
                    if indegree_map[node] == 0:
                        visited.add(node)
                    else:
                        indegree_map[node] -= 1
                else:
                    visited.add(node)
            return True
        
        for course in adjacency_map.keys():
            res = dfs(course)
    return res
numCourses = 20
pre_req = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
result = canFinish(2, [[1,0]])
print(result)