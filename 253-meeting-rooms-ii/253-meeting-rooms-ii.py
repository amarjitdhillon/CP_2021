from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, inter: List[List[int]]) -> int:
    
        # Sort the meeting times by start-times in increasing order
        inter.sort()
        
        '''
        Create an end time min-heap which will hold the end time of the last meeting.
        In other words this time is telling us that after this time, the room will be availabe
        The final result will be the length of such a min-heap
        '''
        endTimeMinHeap = []

        for start, end in inter:
            # If there is nothing in the min-heap then push the current end time, as that would mean we booked a room
            if len(endTimeMinHeap) == 0:
                heappush(endTimeMinHeap, end)
                continue
            # If the current start time for which we want to book a meeting is less than end time, it means we can't use this room to book a meeting  
            elif start < endTimeMinHeap[0]: # Here endTimeMinHeap[0] is the first element of heap representing top of the min-heap
                heappush(endTimeMinHeap, end)
            # Other wise it means that we can book the room. So, we need to update the end time of the top-most element in the min-heap by doing pop and push operation  
            else:
                heappop(endTimeMinHeap)         # Remove the last end time
                heappush(endTimeMinHeap, end)   # Update the end time
        return len(endTimeMinHeap)
            
    
    


    
    
    