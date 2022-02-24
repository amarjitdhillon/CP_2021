# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, a: ListNode, b: ListNode) -> ListNode:
    
        # create a dummy node and let curr point to it initially
        dummy = curr = ListNode(None)
        
        # set carry as 0 initailly
        carry = 0
        
        # proceed while any of the two linked lists are not None
        while(a or b):
            # if this linked list exists, then get the value and update pointer. Else set value = 0
            if a:
                x = a.val
                a = a.next
            else:
                x = 0
                
            if b:
                y = b.val
                b = b.next
            else:
                y = 0
                
            
            # total will be sum of both + carry value
            total = x+y+carry
            
            # if total = 18, then carry is equal to quotient we get when we divide it by 10
            carry = total // 10    
            
            # if total = 18, then sum to be added to node is equal to remainder we get when we divide it by 10
            remainder = total % 10
            
            # create a new node and add remainder to it
            node =  ListNode(remainder)
            
            # point current to this new node and then update current pointer
            curr.next = node
            curr = curr.next
       
        # at the end, if carry is still 1, then add a new node
        if carry == 1:
            curr.next = ListNode(1)
            
        return dummy.next
        