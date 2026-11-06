from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def get_depth(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            # Update the longest path found so far (in terms of edges)
            max_diameter = max(max_diameter, left_depth + right_depth)

            # Return the depth of the subtree rooted at this node
            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return max_diameter