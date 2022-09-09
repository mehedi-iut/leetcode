from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # n = len(edges)
        # parent = []

        # for i in range(n+1):
        #     parent.append(i)

        # res = [0]*2

        # def find(x):
        #     if x != parent[x]:
        #         parent[x]=find(parent[x])
        #     return parent[x]

        # for i in range(n):
        #     x = find(edges[i][0])
        #     y = find(edges[i][1])
        #     if x != y:
        #         parent[y] = x

        #     else:
        #         res[0] = edges[i][0]
        #         res[1] = edges[i][1]

        # return res
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]





edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

sln = Solution()
res = sln.findRedundantConnection(edges)
print(res)