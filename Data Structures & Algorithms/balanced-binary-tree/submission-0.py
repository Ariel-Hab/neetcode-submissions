# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def get_balanced(node: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if not node or not is_balanced:
                return 0

            left_depth = get_balanced(node.left)
            right_depth = get_balanced(node.right)

            dif = abs(right_depth - left_depth)
            if dif > 1:
                is_balanced = False

        # Return the depth of the subtree rooted at this node
            return 1 + max(left_depth, right_depth)

        get_balanced(root)
        return is_balanced