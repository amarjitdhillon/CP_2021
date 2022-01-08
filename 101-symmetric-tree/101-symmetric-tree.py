# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        To be symetric, we have to iterate over the left and right tree simuntaniously 
            - return False if one of them is null while other is not
            - if both are not None, then we will return True if both of values are same. 
            - Return False if both of them exits but values are not same
        
        We can write a recursive function for this
        """
        # As there is no tree
        if not root:
            return False
        
        def checkSymmetric(x, y):
            
            if not x and not y:
                return True
            
            if not x or not y:
                return False
            
            # if both of them are not same
            if x.val != y.val:
                return False
            
            return checkSymmetric(x.left, y.right) and checkSymmetric(x.right, y.left)
                
        return checkSymmetric(root.left, root.right)
        