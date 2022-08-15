pre_req = [[3,1], [2,1], [2,3], [2,4]]

# create the adjacency list
map = {}

for data in pre_req:
    if data[1] in map:
        map[data[1]].append(data[0])
    else:
        map[data[1]] = [data[0]]

print(map)

# Create in-degree map
indegree_map = {}
for data in pre_req:
    if data[0] in indegree_map:
        indegree_map[data[0]] += 1
    else:
        indegree_map[data[0]] = 1

print(indegree_map)

# dfs
visited = set()

def dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node in visited:
            return False
        
        for child in map[node]:
            stack.extend(child)
        
        if indegree_map[node] == 0:
            visited.add(node)
        else:
            indegree_map[node] -= 1


        