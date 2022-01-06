# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """
        To find the loneny nodes, we can do the pre-order traversal and then can return the count if one of node is there while other is None
        """
        self.lonely = []
        
        def inorder(node):
            # base condition
            if not node:
                return None
            
            if not node.left and node.right:
                self.lonely.append(node.right.val)
                
            if not node.right and node.left:
                self.lonely.append(node.left.val)
            
            inorder(node.left)
            inorder(node.right)

        inorder(root)
        return self.lonely