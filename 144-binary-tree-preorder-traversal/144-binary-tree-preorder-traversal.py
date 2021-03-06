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
            # for null node
            if root is None: return
            
            # for leaf node: print it
            result.append(root.val)
                
            # call DFS on left child
            preorder(root.left)

            # call DFS on right child
            preorder(root.right)
        
            return result
        
        return preorder(root)