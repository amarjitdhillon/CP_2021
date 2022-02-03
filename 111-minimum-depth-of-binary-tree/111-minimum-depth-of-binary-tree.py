# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # return 0 for null node
            return 0
        elif not root.left and not root.right: # return 1 for leaf node
            return 1
        elif root.left and not root.right : # call left subtree and return `1+height of subtree`
            return  1+self.minDepth(root.left)  
        elif root.right and not root.left:  #  call right subtree and return `1+height of subtree`
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))   # return and return `1+height of lowwer subtree`