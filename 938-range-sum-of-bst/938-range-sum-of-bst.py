# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        We can do any traveral here and find a solution in O(n) time while doing a simple comparision if that value lies in low,high range and then return the sum
        
        The time complexity can be optimized by ignorr all the left subtree values lower then "low" and all right subtree values grater then "high" value
        """
        
        self.result = 0
        def inorder(root):
            # base condition
            if not root:
                return
            
            if root: 
                if root.left and root.val > low:
                    inorder(root.left)

                if low <= root.val <= high:
                    self.result += root.val

                if root.right and root.val < high:
                    inorder(root.right)
            
        inorder(root)
        return self.result
        