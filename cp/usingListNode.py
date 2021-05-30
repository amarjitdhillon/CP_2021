class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data ):
        node = Node(data,self.head)
        self.head = node

    def insertAtEnd(self, data):
        # if there is no element
        if self.head is None:
            temp = Node(data)
            self.head = temp
            return

        # if there is an element
        itr = self.head
        while(itr):
            if itr.next is None:
                # create a temp node
                temp = Node(data)
                itr.next = temp
                return
            itr = itr.next

    def inserAtPosition(self, data, index):
        # if added at begining
        if index == 0:
            self.insertAtBegining(data)
            return

        cur_index = 0
        itr = self.head
        while(itr):
            if cur_index+1 == index:
                temp = Node(data,itr.next)
                itr.next = temp
                break
            itr = itr.next
            cur_index += 1

        # if the index is large
        if index > cur_index:
            print("The index is out of bound, hence addition aborted")

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        # iterate though the linked list
        itr = self.head
        llstr = ''
        while(itr):
            if itr.next is None:
                llstr += str(itr.data) + " --> Null"
            else:
                llstr += str(itr.data) + " --> "
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtEnd(66)
    ll.insertAtBegining(1)
    ll.insertAtBegining(2)
    ll.insertAtBegining(3)
    ll.insertAtBegining(5)
    ll.insertAtEnd(10)
    ll.insertAtBegining(67)
    ll.inserAtPosition(101,1)
    ll.insertAtEnd(12)
    ll.print()