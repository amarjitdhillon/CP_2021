class Node:

    # Create a tree node as per given data
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # add node to the tree based on the BST login
    def add(self,data):

        # check if the data is not null
        if self.data != None:
            # we can insert in left if this number is less then root's value
            if data < self.data:
                # we can insert in left if there is no node
                if self.left is None:
                    self.left = Node(data)
                else:
                    # else call this function recursively
                    self.left.add(data)
            # we need to insert in the right if this value is higher
            elif data > self.data:
                # if this value is higher, so we can add it to the right side
                if self.right is None:
                    self.right = Node(data)
                else:
                    # call this function recursively
                    self.right.add(data)
            # we need to add data  at this root as no node existed
            else:
                self.data = Node(data)

    # function to do inorder traversal: left --> root --> right
    def inorderTraversal(self, root):
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    # do the pre-order traversal: root --> left --> right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    # postorder traversal: left --> right --> root
    def postorderTraversal(self,root):
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    # Here, we will need a queue to do the BFS.
    def bfs(self,root):
        queue = []
        res = []   # for string the output
        if root:
            queue.append(root)

        while len(queue) > 0:
            # get the first element from the queue
            first = queue.pop(0)
            res.append(first.data)

            # get the left and right nodes of the first element
            left = first.left
            right = first.right

            if left:
                queue.append(left)
            if right:
                queue.append(right)
        return res

if __name__ == '__main__':
    # create a tree node
    tree = Node(12)

    # add elements to the tree node
    tree.add(6)
    tree.add(14)
    tree.add(3)
    tree.add(7)
    tree.add(13)
    tree.add(15)

    '''
    Tree will be like
                      12
                    /   \
                   6     14
                  / \    /  \
                3    7  13  15
    '''
    # print various traversals
    print("  In order =", tree.inorderTraversal(tree))
    print(" Pre order =", tree.preorderTraversal(tree))
    print("Post order =", tree.postorderTraversal(tree))
    print("       BFS =", tree.bfs(tree))