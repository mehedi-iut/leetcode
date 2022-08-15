from collections import defaultdict
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

adj = defaultdict(list)
ind = defaultdict(int)

# build the graph
for frm, to, time in roads:
	adj[frm].append(to)
	adj[to].append(frm)

print(adj)
