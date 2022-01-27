class DLL:
    def __init__(self): # create a node for doubly linked list
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None

    
class LRUCache:
    def addNodeToHead(self, node: DLL):
        # This method will add the current node after head node
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def deleteLastNode(self):
        # we will delete the second last node in this case before tail node
        last = self.tail.prev
        self.deleteNode(last)
        return last      # returning the node as we might want to get the key:val of deleted node
    
    def deleteNode(self, node):
        # This is to deleted a given node, not necessarally the last node
        x = node.prev
        y = node.next
        x.next = y
        y.prev = x
        
    def moveNodeToHead(self, node: DLL):
        '''
        - If a node in accessed using get(), then we need to delete that node and then move it to head to update it's priority
        - We will first delete this node usind deleteNode()
        - Then create this node in front of the head using addNodeToHead()
        '''
        self.deleteNode(node)
        self.addNodeToHead(node)
    
    def __init__(self, capacity: int):
        self.cache = {}             # this hashmap consists of key: address_to_node
        self.capacity = capacity
        self.head = DLL()
        self.tail = DLL()
        
        self.head.next = self.tail   # connecting the head and tail nodes with one another
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        if node exists, then show the value and move it to head
        if node do not exist, then return -1
        """
        node = self.cache.get(key) # get the address of the node
        
        if not node: # if node does not exist in cache
            return -1
    
        # if node exists, then we will move this node to head to update it's priority and return it's value
        self.moveNodeToHead(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        '''
        If node exist then:
            - upate the node value. The way to ckeck if node exists is to check if key in preset in cache hashmap
            - update priority by moving node to front of linked list
        If node does not exist then check the size
            If there is space, then add the node to the head --> update cache
            If no space then delete the node --> then add the node to the head --> update address in cache
        '''
        node = self.cache.get(key)
        
        if node:
            # as node already exists, so we need to update the value and priority
            node.val = value
            self.moveNodeToHead(node) 
        else:
            # create a new node with given key and value
            node = DLL()
            node.key = key
            node.val = value
            
            # add this reference to the cache
            self.cache[key] = node    # save the address of this node to the cache's value
            self.addNodeToHead(node)  # add this node in front of head node. As we have added this node then it might happen that cache size is > capacity 

            if len(self.cache.keys()) == self.capacity+1: # if cache size is one more then the capacity
                temp = self.deleteLastNode() # remove the second last node from DLL before the tail node to make space
                del self.cache[temp.key] # remove the node from cache

                
