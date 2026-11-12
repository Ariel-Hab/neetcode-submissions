class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Un árbol de n nodos SIEMPRE tiene exactamente n - 1 aristas.
        # Si tiene menos, hay nodos huérfanos/separados. Si tiene más, hay ciclos.
        if len(edges) != n - 1:
            return False

        # 2. Construir lista de adyacencia NO DIRIGIDA (bidireccional)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 3. DFS simple para verificar que todos estén conectados desde el nodo 0
        visitados = set()

        def dfs(node: int):
            visitados.add(node)
            for neighbour in adj[node]:
                if neighbour not in visitados:
                    dfs(neighbour)

        dfs(0)

        # Si visitamos todos los n nodos desde el 0, no hay huérfanos ni árboles separados
        return len(visitados) == n
        
        