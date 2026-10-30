# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mi_funcion() -> Optional[ListNode]:
    # Si la lista está vacía, no regresas [], regresas None
    return None

class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node1 = list1
        curr_node2 = list2
        newListPointer = ListNode()
        start = newListPointer
        while curr_node2 is not None and curr_node1 is not None:
            if  curr_node1.val <= curr_node2.val :
                newListPointer.next = curr_node1
                
                curr_node1 = curr_node1.next
            else:
                newListPointer.next = curr_node2
                curr_node2 = curr_node2.next
            
            newListPointer = newListPointer.next
        if curr_node1 is not None:
            newListPointer.next = curr_node1
        elif curr_node2 is not None:
            newListPointer.next = curr_node2
        return start.next
                
            