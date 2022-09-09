stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

parent = [i for i in range(len(stones))]
rank = [1]*len(parent)

def find(n):
    p = parent[n]

    while p != parent[p]:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p


def union(n1, n2):
    p1, p2 = find(n1), find(n2)

    if p1 == p2:
        return
    
    if rank[p1] > rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p1] = p2
        rank[p2] += rank[p1]

n = len(stones)

ans = 0

for i in range(n):
    for j in range(i+1, n):
        if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
            union(i, j)

for i in range(len(parent)):
    if i != parent[i]:
        ans += 1
print(ans)