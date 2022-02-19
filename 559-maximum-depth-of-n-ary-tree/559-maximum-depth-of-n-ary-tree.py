"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case for leaf node
        if root is None:
            return 0
        # Here children is a list of all the childrens
        # If that is empty it means we should return 1 as dephh of parent node
        elif root.children == []:
            return 1
        else:
            # Otherwise, we do DFS for all the childrens and return the max depth of a children
            # We will use a depths list to store the depth of all all subtrees
            depths = []
            # Loop over all the childrens 
            for child in root.children:
                # Call this function recursively and save the depth in the depth array
                depths.append(self.maxDepth(child))
            # After all childrens are iterated, return the max depth
            return max(depths)+1
        