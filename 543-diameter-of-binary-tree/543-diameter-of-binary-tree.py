# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        
        def dfs(root):
            nonlocal dia # a non local variable
            
            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            
            dia = max(dia, lh+rh)
            
            return 1 + max(lh,rh) 
        
        dfs(root)
        return dia
        