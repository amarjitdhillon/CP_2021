class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self,data):
        if self.data != None: # checking if the data is not null
            if data < self.data: # we can insert in left
                if self.left is None: # means we can insert in left
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data: # we need to insert in the right
                if self.right is None: # add it to the left immediately
                    self.right = Node(data)
                else:
                    self.right.add(data)
            else: # we need to add data  at this root
                self.data = Node(data)

    def inorderTraversal(self, root):
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self,root):
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    def dfs(self,root):
        queue = []
        res = []   # for string the output
        if root:
            queue.append(root)

        while len(queue) > 0:
            first = queue.pop(0)     # get the first element from the queue
            res.append(first.data)

            left = first.left       # get the left and right nodes of the first element
            right = first.right

            if left:
                queue.append(left)
            if right:
                queue.append(right)
        return res

if __name__ == '__main__':
    tree = Node(12)
    tree.add(6)
    tree.add(14)
    tree.add(3)
    tree.add(7)
    tree.add(13)
    tree.add(15)

    print("  In order =", tree.inorderTraversal(tree))
    print(" Pre order =", tree.preorderTraversal(tree))
    print("Post order =", tree.postorderTraversal(tree))
    print("       BFS =", tree.dfs(tree))