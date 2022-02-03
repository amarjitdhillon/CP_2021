# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q: # both of the nodes can be null at same time
            return True
        
        if not p or not q: # either of the nodes can not be null as that will mean tree is not equal
            return False
        
        if p.val != q.val: # if both nodes exists, then code will reach till here. Now if both values are not same then return False
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # repeat this process for left and right tree