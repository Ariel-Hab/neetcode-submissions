class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        # 1. Start with all leaf nodes (degree == 1)
        leaves = deque([node for node in graph if len(graph[node]) == 1])
        
        # 2. Peel away all branches until only the cycle remains
        while leaves:
            leaf = leaves.popleft()
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)
                
        # 3. Any node left with degree > 0 is part of the cycle.
        # Scan edges from the back to find the last edge in the cycle.
        for u, v in reversed(edges):
            if len(graph[u]) > 0 and len(graph[v]) > 0:
                return [u, v]
                
        return []