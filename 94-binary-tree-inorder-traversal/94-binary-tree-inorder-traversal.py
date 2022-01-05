# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs_inorder(root):
            # terminating condition
            if root is None:
                return 
            
            # print left
            if root.left:
                dfs_inorder(root.left)
                    
            # add root
            if root:
                result.append(root.val)
            
            # add right node
            if root.right:
                dfs_inorder(root.right)
            
        dfs_inorder(root)
        return result
        