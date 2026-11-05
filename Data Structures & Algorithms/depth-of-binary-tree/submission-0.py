# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxL,maxR = 0,0
        if root:
            maxL = self.maxDepth(root.left)
            maxR = self.maxDepth(root.right)
            return(max(maxL,maxR)+1)
        else:
            return 0