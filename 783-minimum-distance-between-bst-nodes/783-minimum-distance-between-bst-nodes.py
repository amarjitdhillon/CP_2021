# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        The min diff can be seen among the left, root node or root,right node
        We can do the inorder traveral and upate the mindiff variable accordingly
        At the end of in-order traversal, we can return the minDiff variable
        """
        
        self.diff = math.inf
        self.prev = -math.inf
        
        def inorder(root):
             if root:
                inorder(root.left)
                self.diff = min(self.diff, root.val - self.prev)
                self.prev = root.val
                inorder(root.right)

                
        inorder(root)
        return self.diff
                
                
            