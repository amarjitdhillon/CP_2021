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


    def printLinkedList(self,head):
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

    def mergeTwoLists(self,listA, listB):
        head = None
        p1 = listA  # pointer for first linked list
        p2 = listB  # pointer for second linked list

        if p1.next is None and p2.next is None:
            return head

        while True:
            if p1 is None and p2 is None:
                return head

            if p1 is None:
                curr.next = p2
                return head

            if p2 is None:
                curr.next = p1
                return head

            if p1.val == p2.val:
                temp = Node(p2.val)
                if head == None:
                    head = temp # as this is the first node
                    curr = head
                curr.next = temp
                curr.next.next = temp
                curr = curr.next.next  # update the curr pointer

                p1 = p1.next
                p2 = p2.next

            elif p1.val < p2.val:
                temp = Node(p1.val)
                if head == None:
                    head = temp  # as this is the fist node
                    curr = head
                curr.next = temp  # add the smallest node to the result linked list
                curr = curr.next  # update the current pointer
                p1 = p1.next  # move p1 to next node as we have added it to result

            else:
                temp = Node(p2.val)
                if head == None:
                    head = temp
                    curr = head
                curr.next = temp
                p2 = p2.next


if __name__ == '__main__':

    llistA = LinkedList()
    llistA.addAtEnd(1)
    llistA.addAtEnd(1)
    llistA.addAtEnd(8)
    llistA.printLinkedList(llistA.head)

    llistB = LinkedList()
    llistB.addAtEnd(7)
    llistB.addAtEnd(8)
    llistB.addAtEnd(10)
    llistB.printLinkedList(llistB.head)

    resultHead = llistB.mergeTwoLists(llistA.head,llistB.head)
    llistB.printLinkedList(resultHead)