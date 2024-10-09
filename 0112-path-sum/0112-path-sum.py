# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Call Dfs on the root and have a current sum dfs will return a bool
        #if that node is false we will return False
        #else we would add the node.val to the CurSum
        #if there are no left and right node then we know we are at the end
        #if we are at the end then we need to check if the current sum is equal to the target sum
        
        def dfs(node, curSum):
            if node == None:
                return False
            
            curSum += node.val
            
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
                return False
                
                
            return (dfs(node.left,curSum) or dfs(node.right,curSum))
                
            
        return dfs(root,0)
            

        