from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, inter: List[List[int]]) -> int:
    
        # sort the meeting times by start-tiems
        inter.sort()
        
        # create an end time min-heap which will hold the end time of the last meeting.
        # in other words this time is telling us that after this time, the room will be availabe
        # The final result will be the length of such a min-heap
        endTimeMinHeap = []

        for start, end in inter:
            # if there is nothing in the min-heap then push the current end time, as that would mean we booked a room
            if len(endTimeMinHeap) == 0:
                heappush(endTimeMinHeap, end)
                continue
            # if the current start time for which we want to book a meeting is less than end time, it means we can't use this room to book a meeting  
            elif start < endTimeMinHeap[0]: # here endTimeMinHeap[0] is the first element of heap representing top of the min-heap
                heappush(endTimeMinHeap, end)
            # other wise it means that we can book the room. So, we need to update the end time of the top-most element in the min-heap by doing pop and push operation  
            else:
                heappop(endTimeMinHeap)         # remove the last end time
                heappush(endTimeMinHeap, end)   # update the end time
        return len(endTimeMinHeap)
            
    
    


    
    
    