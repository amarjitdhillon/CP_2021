# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        # A list will store all the node references in an inorder traversal
        r = []

        # DFS traversal for inorder traversal
        def dfs(root):
            # base case
            if not root:
                return
            
            # add root to list, then call left and right
            r.append(root)
            # store the reference of left and right to the list. Here we are storing reference not the values
            dfs(root.left)
            dfs(root.right)

        # driver code
        dfs(root)
        
        root = r[0]
        curr = root
        
        for x in range(1,len(r)):
            # left node is always null as per condition in the question
            curr.left = None
            # populate right with the next value and then update right pointer to next
            curr.right = r[x]
            curr = curr.right
            