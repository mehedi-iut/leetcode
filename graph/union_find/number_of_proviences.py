
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

parent = [i for i in range(len(isConnected))]
rank = [1]*len(isConnected)

def find(n):
    p = parent[n]

    while p != parent[p]:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p

def union(n1, n2):
    p1, p2 = find(n1), find(n2)

    if p1 == p2:
        return 0
    
    if rank[p1] > rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p2] = p1
        rank[p1] += rank[p2]
    
    return 1

count = len(isConnected)

for i in range(len(isConnected)):
    for j in range(len(isConnected[i])):
        if isConnected[i][j] == 1:
            count -= union(i, j)

print(count)