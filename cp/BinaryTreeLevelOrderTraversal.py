'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

'''
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def levelOrderTraversal(self ,root):

        first_queue     = []
        second_queue    = []
        result          = []          # this will hold the nodes

        if root is None:
            return result
        else:
            first_queue.append(root)

        # we will use the BFS here, so we are using the queue
        while (len(first_queue) > 0 or len(second_queue) > 0):

            if (len(first_queue)) == 0:
                first_queue  = second_queue
                second_queue = []

            temp = []

            while(len(first_queue) > 0):
                node = first_queue.pop(0)  # get the first element in the queue

                if node.left is not None: # means right tree exists
                    second_queue.append(node.left)
                if node.right is not None:
                    second_queue.append(node.right)
                temp.append(node.data)
            result.append(temp)
        return result


if __name__ == '__main__':
    root            = Node(1)
    root.left       = Node(2)
    root.right      = Node(3)
    root.left.left  = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(root.levelOrderTraversal(root))
