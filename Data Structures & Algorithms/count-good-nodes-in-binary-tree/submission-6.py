# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:       
        def amountGoodNodes(root:TreeNode, maxVal:int)->int:
            counter = 0
            if root.val >= maxVal:
                counter += 1
                maxVal = root.val
            if(root.left):
                counter += amountGoodNodes(root.left, maxVal)
            if(root.right):
                counter += amountGoodNodes(root.right, maxVal)

            return counter
        
        return amountGoodNodes(root,root.val)




