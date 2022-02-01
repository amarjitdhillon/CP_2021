# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        We are using 3 pointers here: prev, curr and ahead
        '''
        prev, curr, ahead = None, head, None
        while curr:
            ahead       = curr.next # save the reference
            curr.next   = prev      # update curr pointer
            prev        = curr      # update reference for prev and curr
            curr        = ahead
        return prev                 # as curr is pointing to None, so prev is pointing to head
    