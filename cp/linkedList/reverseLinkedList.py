class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    # insert to the end of the linkedList
    def addAtEnd(self, data):
        # add to the begining if there is no item
        if self.head is None:
            self.head = Node(data)
            return

        # else we need to iterate over the linked list
        curr = self.head
        while(curr.next):
            curr = curr.next # move the curr to next item
        curr.next = Node(data) # we have reached the last node


    def printList(self,head):
        result = []
        if head is None:
            return  result
        else:
            curr = head
            while(curr.next):
                result.append(curr.val)
                curr = curr.next
            result.append(curr.val)
        print(result)

    def reverseLinkedList(self):
        prev = None
        curr = self.head

        while(curr is not None):
            next        = curr.next # populate the next value
            curr.next   = prev
            prev        = curr
            curr        = next

        self.head = prev # this is for the last node

        self.printList(self.head)

if __name__ == '__main__':

    llist = LinkedList()
    llist.addAtEnd(1)
    llist.addAtEnd(2)
    llist.addAtEnd(3)
    llist.addAtEnd(4)

    llist.printList(llist.head)   # print the original list
    llist.reverseLinkedList()     # reverse the list and print
