class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Nodes are 1-indexed from 1 to len(edges)
        parent = list(range(len(edges) + 1))
        
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]
        
        def union(u: int, v: int) -> bool:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False  # Already connected -> cycle found
            parent[root_u] = root_v
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
                
        return []