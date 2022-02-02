import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        r = 0
        
        heapq._heapify_max(stones)
        while(len(stones) > 1): # at least 2 stones are needed
            x=  heapq.heappop(stones) # remove first item
            heapq._heapify_max(stones)
            
            y = heapq.heappop(stones) # remove second item
            r = abs(x-y)
            
            heapq.heappush(stones,r)  # add r to stones heap
            heapq._heapify_max(stones)
        return r