n = 4
edges = [[1, 0], [1, 2], [1, 3]]
# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]


# build the adjacency list
adj = {}
indegree = {u:0 for u in range(n)}

for i in range(n):
	if i not in adj.keys():
		adj[i] = []

# build indegree
for to, frm in edges:
	adj[frm].append(to)
	indegree[to] += 1

empty_list = [ele[0] for ele in adj.items() if ele[1] == []]

print(adj)
print(indegree)
print(empty_list)

q = [element for element in indegree if indegree[element] == 0]
top_sort = []

while q:
	node = q.pop(0)
	top_sort.append(node)

	for data in adj[node]:
		indegree[data] -= 1
		if indegree[data] == 0:
			q.append(data)



print("top sort: {}".format(top_sort))

empty_index = []
for i in empty_list:
	empty_index.append(i)

empty_index.sort()

root_min = []
root_min.append(empty_index[0])

for i in adj.keys():
	if adj[i] == empty_list:
		root_min.append(i)

print(root_min)
