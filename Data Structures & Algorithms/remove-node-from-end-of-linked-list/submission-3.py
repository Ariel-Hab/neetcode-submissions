# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        n_pointer = head
        counter = 0
        while pointer.next is not None:
            pointer = pointer.next
            if counter != n:
                counter += 1
            else: 
                n_pointer = n_pointer.next
        if counter < n:
            return head.next
            
        n_pointer.next = n_pointer.next.next
        return head

            
        
            