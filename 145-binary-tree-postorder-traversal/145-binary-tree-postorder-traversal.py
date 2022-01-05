# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def postorder(root):
            # Order of traversal is left --> right --> root 
            # base condition
            if not root:
                return
            
            if root.left:
                postorder(root.left)
                
            if root.right:
                postorder(root.right)
                
            if root:
                result.append(root.val)
                
            return result
            
        return postorder(root)
            
            
        