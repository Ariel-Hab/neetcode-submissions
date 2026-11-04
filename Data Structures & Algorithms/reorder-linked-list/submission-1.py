# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:       
        current = head 
        while current.next and current.next.next:
            
            penultimo = current
            while penultimo.next.next is not None:
                penultimo = penultimo.next
            last = penultimo.next
            penultimo.next = None

            next_node = current.next
            current.next = last
            current = current.next
            current.next = next_node
            current = current.next
            
            
