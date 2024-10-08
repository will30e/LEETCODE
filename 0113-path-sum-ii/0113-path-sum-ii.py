# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        if not root:
            return []
        def dfs(node,path,sm):
            sm+=node.val
            tmp=path+[node.val]
            if node.right:
                dfs(node.right,tmp,sm)
            if node.left:
                dfs(node.left,tmp,sm)
                
            if not node.right and not node.left and sm == targetSum:
                output.append(tmp)
                
                
        dfs(root,[],0)
        return output
                