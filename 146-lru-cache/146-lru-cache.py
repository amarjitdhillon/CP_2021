class DLL:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None

    
class LRUCache:
    def addNodeToHead(self, node: DLL):
        # here we will add the current node after head node
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        return node
        
    def deleteLastNode(self):
        # we will delete the last node in this case
        last = self.tail.prev
        self.deleteNode(last)
        return last
    
    def deleteNode(self, node):
        x = node.prev
        y = node.next
        x.next = y
        y.prev = x
        
    def moveNodeToHead(self, node: DLL):
        '''
        - If a node in accessed, then we need to delete that node and then move it to head
        - We will first delete this node 
        - Then create this node in front of the head
        '''
        self.deleteNode(node)
        self.addNodeToHead(node)
    
    def __init__(self, capacity: int):
        self.cache = {} # this hashmap consists of key: address_to_node
        self.capacity = capacity
        self.head = DLL()
        self.tail = DLL()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        if node exists, then show the value and move it to head
        if node do not exist, then return -1
        """
        # get the address of the node
        node = self.cache.get(key)
        
        if not node:
            return -1
    
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
            # we need to update the value and update the priority
            node.val = value
            self.moveNodeToHead(node) 
        else:
            # create a node
            node = DLL()
            node.key = key
            node.val = value
            
            # add this reference to the cache
            self.cache[key] = node
            self.addNodeToHead(node)

            if len(self.cache.keys()) > self.capacity:
                # remove the pre-tail node from DLL
                temp = self.deleteLastNode()
                
                # remove the node from cache
                del self.cache[temp.key]

                
