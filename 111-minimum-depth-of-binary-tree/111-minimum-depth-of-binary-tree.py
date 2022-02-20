# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # return 0 for null node
        if not root:  return 0
        
        # return 1 for the leaf node
        elif not root.left and not root.right: return 1
        
        # call left subtree and return `1+height of left subtree`
        elif not root.right : return  1+self.minDepth(root.left)
        
        #  call right subtree and return `1+height of right subtree`
        elif not root.left:  return 1+self.minDepth(root.right)
        
        # If both left and right subtree exists then, return `1+height of lower subtree`
        else: return 1+min(self.minDepth(root.left),self.minDepth(root.right))   