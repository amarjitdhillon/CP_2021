# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        # both the pointers are pointing to the head
        # the intution is that when fast will reach the end of linked list, the slow will point to the middle of the list
        fast = head
        slow = head 
        
        # as slow is equal to fast.next, so we are checking if both slow and fast are not null
        while fast and fast.next:
            fast = fast.next.next   # jump by 2 hops
            slow = slow.next        # jump by 1 hop
        return slow                 # as it points to the middle of the list