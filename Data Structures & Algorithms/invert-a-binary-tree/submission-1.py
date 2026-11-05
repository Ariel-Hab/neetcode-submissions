# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # the key is in what method to read the tree they used
        if root:
            store_left = root.left
            root.left = root.right
            self.invertTree(root.left)
            root.right = store_left
            self.invertTree(root.right)
        return root