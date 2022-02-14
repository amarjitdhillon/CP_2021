from heapq import heapify, heappush, heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minCost, minHeap = 0, sticks
        
        # edge case 
        if len(sticks) == 0 or len(sticks) == 1:
            return minCost
        
        heapify(minHeap)
        
        while(len(minHeap) > 1):
            x = heappop(minHeap)
            y = heappop(minHeap)
            z = x+y
            minCost += z 
            heappush(minHeap,z)
  
            
        return minCost
            