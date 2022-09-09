class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjacency = collections.defaultdict(list)
        for x,y in edges:
            adjacency[x].append(y)
            adjacency[y].append(x)
        
        
        def dfs(src, target, path, visited):
            path.append(src)
            visited.add(src)
            
            if src == target:
                return path
            
            for neighbor in adjacency[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, path, visited)
                
                    if result is not None:
                        return True
            
            path.pop()
            return False
        
        dfs(source, destination, path=[], visited=set())