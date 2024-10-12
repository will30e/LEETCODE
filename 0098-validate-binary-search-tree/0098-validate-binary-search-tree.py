# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            # The current node's value must be within the range (left, right)
            if not (left < node.val < right):
                return False

            # Recursively check the left and right subtrees with updated boundaries
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # Start the recursion with the root and the initial range (-∞, +∞)
        return valid(root, float("-inf"), float("inf"))

