# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Order of traversal is left --> right --> root 
        def postorder(root):
            
            # base condition for null node 
            if not root: return
            
            # call DFS on left subtree
            postorder(root.left)
                
            # call DFS on right subtree
            postorder(root.right)
                
            # all root node value to list
            result.append(root.val)
                
            return result
        
        # driver code
        return postorder(root)
            
            
        