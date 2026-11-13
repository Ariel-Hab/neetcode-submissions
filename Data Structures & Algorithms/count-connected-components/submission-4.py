class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        # state = [[0] for _ in range(n)]
        for node, link in edges:
            adj[node].append(link)
            adj[link].append(node)
        visitados = set()
        def walkComponent(node):
            # if state[node] == 1:
            #     return
            nonlocal visitados
            if (node) in visitados:
                return
            visitados.add((node))
            # if state[node] == 2:
            #     return
            # state[node] = 1
            for neigh in adj[node]:
                print(neigh)
                walkComponent(neigh)
        c = 0
        for node in range(n):
            print(node)
            if (node) not in visitados:
                print(node)
                c+=1
                walkComponent(node)
        return c