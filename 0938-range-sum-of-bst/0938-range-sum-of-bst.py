# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: if the current node is None, return 0
        if root is None:
            return 0
        
        # Initialize the sum
        total_sum = 0
        
        # Check if the current node's value is within the range
        if low <= root.val <= high:
            total_sum += root.val
        
        # If the current node's value is greater than low, search the left subtree
        if root.val > low:
            total_sum += self.rangeSumBST(root.left, low, high)
        
        # If the current node's value is less than high, search the right subtree
        if root.val < high:
            total_sum += self.rangeSumBST(root.right, low, high)
        
        # Return the total sum of values within the range
        return total_sum
        