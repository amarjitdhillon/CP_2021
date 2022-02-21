class MinStack:

    # MinStack() initializes the stack object
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []     # this will hold the main stack elements
        self.mstack = []    # this will hold the mininum value
    
    # push(int val) pushes the element val onto the stack.
    def push(self, val: int) -> None:
        # Always add the number in the main stack.
        self.stack.append(val)
        
         # If this is the min stack is empty or this is the smaller nunber then current top in main stack, then add this value to minstack 
        if len(self.mstack) == 0 or val < self.mstack[-1][0]:
            self.mstack.append([val,1])
            # Else if this number is equal to what's currently at the top of the min stack, then increment the count at the top by 1.
        elif val == self.mstack[-1][0]:
            self.mstack[-1][1] += 1

    # pop() removes the element on the top of the stack.
    def pop(self) -> None:
        # we need to compare the top of min stack and top of main stack
        # if the top of min stack is same as the top of the main stack, then we need to decrement the count
        if self.mstack[-1][0] == self.stack[-1]:
            self.mstack[-1][1] -= 1
            
        # if the count at the top of the min stack is 0, then remove it
        if self.mstack[-1][1] == 0:
            self.mstack.pop()
            
        # pop value from the main stack
        self.stack.pop()
        
    
    # top() gets the top element of the stack (but doesn't remove) the top value of the main Stack
    def top(self) -> int:
        # This is a seek operation, so just optput the last element in the list
        return self.stack[-1]    
    
    # getMin() retrieves the minimum element in the stack but doesn't remove. Here we have to use the min stack
    def getMin(self) -> int:
        return self.mstack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()