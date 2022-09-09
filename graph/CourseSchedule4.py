import collections
numCourses = 4
prerequisites = [[2,3],[2,1],[0,3],[0,1]]
queries = [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]




# ind = [0 for _ in range(numCourses)]
# q = []
# adj = collections.defaultdict(list)
# arr = []

adj = {node: set() for node in range(numCourses)}
ind = collections.defaultdict(int)
pre_lookup = collections.defaultdict(set)
q = []

# build the graph
for u,v in prerequisites:
	adj[u].add(v)
	ind[v] += 1

for i in range(numCourses):
	if ind[i] == 0:
		q.append(i)


while q:
	node = q.pop(0)

	for vertex in adj[node]:

		pre_lookup[vertex].add(node)
		pre_lookup[vertex].update(pre_lookup[node])

		ind[vertex] -= 1
		if ind[vertex] == 0:
			q.append(vertex)

print(pre_lookup)

result = [True if q[0] in pre_lookup[q[1]] else False for q in queries]
print(result)