# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        pointer = head
        while pointer is not None:
            if pointer in visited:
                return True
            else: 
                visited.add(pointer)
                pointer = pointer.next
        return False