# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0       # we will make this variable as global using non-local
        def dfs(root):
            nonlocal dia # a non local variable
            
            if not root: # null case
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            
            dia = max(dia, lh+rh)  # update the diameter but don't return it
            
            return 1 + max(lh,rh)  # return the depth of subtree
        
        dfs(root)  # calling this fn will update the diameter of the tree
        return dia
        