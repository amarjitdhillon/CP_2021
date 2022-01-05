# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def preorder(root):
        
            # base condition
            if root is None:
                return
            
            if root:
                result.append(root.val)
                
            if root.left:
                preorder(root.left)

            if root.right:
                preorder(root.right)
        
            return result
        
        return preorder(root)