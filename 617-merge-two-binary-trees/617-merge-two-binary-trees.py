# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
        def preorder(x,y):
            if not x :
                return y
            
            if not y:
                return x
            
            t = TreeNode(x.val+y.val)   
            t.left  = preorder(x.left,y.left)
            t.right = preorder(x.right,y.right)
            return t

        return preorder(root1,root2)
