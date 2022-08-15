# here the main idea is, in any given time in queue we have more than one
# element present, then there can be more than one solution exists
# because we can go any direction and get the topological sort.

# Again, when creating the adjacency list, here we have more than two elements
# in the given seqs, we need two for loop to construct the pair and add to the
# adjacency list 




from collections import defaultdict
from functools import reduce
org = [1,2,3]
seqs = [[1,2],[1,3], [2,3]]

from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        nodes = reduce(set.union, seqs, set())
        if nodes != set(org): return False

        n = len(org)
        # build the graph
        adj = defaultdict(list)
        ind = [0 for _ in range(n+1)]
        q = []
        topsort = []

        for seq in seqs:
            for frm, to in zip(seq, seq[1:]):
                adj[frm].append(to)
                ind[to] += 1
        
        q = [ele for ele in org if ind[ele] == 0]

        while q:
            if len(q) > 1: return False

            node = q.pop(0)
            topsort.append(node)

            for neg in adj[node]:
                ind[neg] -= 1
                if ind[neg] == 0:
                    q.append(neg)
        
        return org == topsort

re_obj = Solution()
print(re_obj.sequence_reconstruction(org, seqs))


