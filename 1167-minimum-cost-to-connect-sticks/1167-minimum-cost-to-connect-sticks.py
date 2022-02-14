from heapq import heapify, heappush, heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # create a min-heap and add the sticks to it
        minCost, minHeap = 0, sticks
        
        # edge case 
        if len(sticks) == 0 or len(sticks) == 1:
            return minCost
        
        # min-heapify the sticks
        heapify(minHeap)
        
        # merge sticks unless, minHeap has more than one element
        while(len(minHeap) > 1):
            # get the 2 minimum elements from heap
            x,y  = heappop(minHeap), heappop(minHeap)
            
            # merge the smallest sticks
            z = x+y
            
            # update the cost
            minCost += z 
            
            # add the merged stick to the min-heap
            heappush(minHeap,z)  
        return minCost
            