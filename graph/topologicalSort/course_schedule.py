from collections import defaultdict
numCourses = 2
pre = [[1,0]]

adj = defaultdict(list)

for to, frm in pre:
    adj[frm].append(to)


def dfs(i, adj, stack, visited):
    if i in stack:
        return True
    if i in visited:
        return False

    visited.add(i)
    
    for neg in adj[i]:
        if not dfs(neg, adj, stack, visited):
            return False
    visited.remove(i)
    stack.append(i)
    return True

def top_sort(numCourses, adj):
    stack = []
    visited =set()
    
    for i in range(numCourses):
        if i not in visited:
            if not dfs(i, adj, stack, visited):
                return []
    
    top_sort = stack[::-1]
    return top_sort

print(top_sort(numCourses, adj))




