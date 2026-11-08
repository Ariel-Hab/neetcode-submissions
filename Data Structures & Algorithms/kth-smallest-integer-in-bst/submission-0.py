# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        result = 0
        def recorrer(root):
            nonlocal counter
            nonlocal result
            if not root and result != 0:
                return 
            
            if root.left:
                recorrer(root.left)  
            counter -= 1
            if counter==0:
                result = root.val
                return 
            if root.right:
                recorrer(root.right)
            print(counter)
            print(root.val)
            return 
        recorrer(root)
        return result