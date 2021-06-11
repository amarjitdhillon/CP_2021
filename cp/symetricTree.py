
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def isSymetric(self ,left, right ):

        if(left is None and right is None):
            return True

        if left is not None and right is not None:
            if left.data == right.data:
                return self.isSymetric(left.left,right.right) and self.isSymetric(left.right,right.left)

        return False


if __name__ == '__main__':


    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    # root.left.left = Node(3)
    # root.left.right = Node(4)
    # root.right.left = Node(5)
    # root.right.right = Node(3)


    print(root.isSymetric(root.left,root.right))
