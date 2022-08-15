from collections import defaultdict

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"],["a","e"], ["a", "a"], ["x", "x"]]


graph = defaultdict(dict)

for (x,y), val in zip(equations, values):
	graph[x][y] = val
	graph[y][x] = 1 / val

print(graph)

def dfs(x, y, visited):
	if x not in graph or y not in graph: return -1

	if y in graph[x]:
		return graph[x][y]

	for neg in graph[x]:
		if neg not in visited:
			visited.add(neg)
			temp = dfs(neg, y, visited)
			if temp == -1:
				continue
			else:
				return temp * graph[x][neg]
	return -1

output = []
for p, q in queries:
	output.append(dfs(p,q,set()))
print(output)




