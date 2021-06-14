'''

669
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.


Example 1:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Example 3:
Input: root = [1], low = 1, high = 2
Output: [1]

Example 4:
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Example 5:
Input: root = [1,null,2], low = 2, high = 4
Output: [2]
'''
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def trimBST(self ,root,low, high):
        if root is None:
            return result
        else:
            rv = root.val

        if low <= rv or high >= rv: # add the value to result if condition is met
            result.append(rv)

        if low <= rv and high < rv: # solution is in right and we need to add null to left
            if root.left:
                self.trmBST(root.left,low,high)
                result.append(None)

        elif low >= rv and high > rv: # solution is in right
            result.append(None)
            if root.right:
                self.trimBST(root.right,low,high)

        elif low <= rv and high >= rv: # check both sides
            if root.left:
                self.trimBST(root.left,low,high)
            if root.right:
                self.trimBST(root.right,low,high)

        return result


if __name__ == '__main__':
    #  root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    root            = Node(1)
    root.left       = Node(None)
    root.right      = Node(2)
    # root.left.left  = Node(None)
    # root.left.right = Node(2)
    # root.right.left = Node(None)
    # root.right.right = Node(None)
    # root.left.left.left = Node(1)

    low = 2
    high = 4
    result = []
    print(root.trimBST(root,low, high))
