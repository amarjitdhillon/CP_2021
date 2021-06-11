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

    def rangeSum(self,root,low,high):
        # we are using the BFS here as its easy to do the sum without recursion
        queue = []
        sum = 0
        if root:
            queue.append(root)

        while len(queue) > 0:
            # get the first value
            first = queue.pop(0)
            if low <= first.data <= high:
                sum += int(first.data)
            if first.left:
                queue.append(first.left)
            if first.right:
                queue.append(first.right)
        return sum

if __name__ == '__main__':
    tree = Node(12)
    tree.add(6)
    tree.add(14)
    tree.add(3)
    tree.add(7)
    tree.add(13)
    tree.add(15)
    low = 16
    high = 15

    sum = 0
    result = tree.rangeSum(tree,low,high)
    print(f"Sum of all the values between {low} and {high} (both inclusive) is {result}")