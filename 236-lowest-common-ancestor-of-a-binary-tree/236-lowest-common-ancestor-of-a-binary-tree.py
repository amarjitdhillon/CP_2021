# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root or root == p or root == q:
            return root
        
        x = self.lowestCommonAncestor(root.left, p, q)
        y = self.lowestCommonAncestor(root.right, p, q)
        
        if (x and y) or root in [p,q]:
            return root
        else:
            return x or y
        