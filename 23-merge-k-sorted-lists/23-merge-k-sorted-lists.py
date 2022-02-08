# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a min heap and add the first element of each linked list with the id. here `id` is the list number
        minheap = []
        
        # add the first elements of each linked list in the minheap
        for i,ll in enumerate(lists): # i is index and ll in linked list
            if ll:
                heapq.heappush(minheap, (ll.val,i))
            
        
        root = ListNode()  # create a root node for the output linked list
        curr = root     
        
        # extract min element from each linked list until all of the linked list are not traversed. 
        # We will know all of them are traversed once the minheap is empty as each node in minheap holds a reference to the ll element
        while minheap:
            val, i = heapq.heappop(minheap) # get the min element and it's list #
            
            # add the min node to the result linked list and update the current pointer
            curr.next = ListNode(val)
            curr = curr.next
            
            # update the linked list pointer based on the index of the linked list. Here i is the index of the current LL having lowest value
            lists[i] = lists[i].next 
            
            # after updating the pointer to the linked list, if it's not null, then we will update the heap pointer
            # if the ll is pointing to null, then no need to update heap as we have already poped the lowest node element.
            if lists[i]: 
                heapq.heappush(minheap, (lists[i].val,i))
            
        return root.next # as root was a dummy node