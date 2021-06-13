'''
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


'''
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def minDepth(self ,root):

        queue = []          # this will hold the nodes
        depth = 0

        if root is None:
            return depth
        else:
            depth = 1      # As we have the root, so depth is 1 atleast

        queue.append({'node': root, 'depth': depth})

        # we will use the BFS here, so we are using the queue
        while (len(queue) > 0):
            data_tuple = queue.pop(0)  # get the first element in the queue

            node  = data_tuple['node']
            depth = data_tuple['depth']

            if node.left is None and node.right is None:
                return depth
            if node.left is not None: # means right tree exists
                queue.append({'node': node.left, 'depth': depth+1})
            if node.right is not None:
                queue.append({'node': node.right, 'depth': depth+1})
        return depth


if __name__ == '__main__':
    # [3, 9, 20, null, null, 15, 7]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(None)
    root.right.left = Node(None)
    root.right.right = Node(3)


    print(root.minDepth(root))
