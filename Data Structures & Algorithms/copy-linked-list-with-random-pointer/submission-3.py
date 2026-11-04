"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None  
        pairs = {}
        prev_node = None
        start = head
        while head:
            if head in pairs:
                new_node = pairs[head]
            else:
                new_node = Node(head.val)
                pairs[head] = new_node

            if prev_node:
                prev_node.next = new_node

            if head.random is not None:
                if head.random not in pairs:
                    pairs[head.random] = Node(head.random.val)  # genero entrada
                new_node.random = pairs[head.random]

            prev_node = new_node
            head = head.next
        return pairs[start]