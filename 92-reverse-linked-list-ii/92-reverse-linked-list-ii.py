# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # this is used to handle the case when left == 1, as we add the dummy case before head, so dummy.next will be head in edge cases
        
        beg, last, curr, prev = dummy, None, head, None
        
        # find the reference for left node
        for _ in range(left-1):
            beg     = curr
            curr    = curr.next
        
        # reverse the node from left to right
        for _ in range(right - left + 1):
            y           = curr.next   # save the reference
            curr.next   = prev 
            prev        = curr        # reversed left node after end of this loop 
            curr        = y           # node after right position at end of this loop
            
        # update the reference for beg and curr node
        beg.next.next   = curr
        beg.next        = prev
        
        return dummy.next
        
        
            