# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # base case: when we reach leaf node, then we will return 0
        if root == None:
            return 0
        
        # call left and right subtree and save the result in some variable 
        lelt_height     = self.maxDepth(root.left)
        right_height    = self.maxDepth(root.right)
        
        # The max height of this subtree is max height of it's left or right subtree
        return 1+ max(lelt_height,right_height)
        