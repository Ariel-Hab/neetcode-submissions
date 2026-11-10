"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        related = {}
        def dfs(node:'Node')->'Node':
            nonlocal related
            if node in related:
                return related[node]
            copy = Node(node.val)
            related[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        newNode = dfs(node)
        return newNode
        
            