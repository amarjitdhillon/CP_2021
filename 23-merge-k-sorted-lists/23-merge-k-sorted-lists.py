# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a min heap and add the first element of each LL with the id. here `id` is the list number
        minheap = []
        
        # add the first elemnets in minheap
        for i,ll in enumerate(lists): # i is index and ll in linked list
            if ll:
                heapq.heappush(minheap, (ll.val,i))
            
        # create a root node
        root = ListNode()
        curr = root
        
        # extract min element
        while minheap:
            val, i = heapq.heappop(minheap)
            
            # add it to the result linked list
            curr.next = ListNode(val)
            curr = curr.next
            
            # update the heap pointer based on the index of the linked list
            lists[i] = lists[i].next 
            
            # udate the heap with next value
            if lists[i]: 
                heapq.heappush(minheap, (lists[i].val,i))
            
        return root.next