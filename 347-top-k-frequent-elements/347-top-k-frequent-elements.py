from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1: # edge case
            return nums
        
        # build a dict
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] = hm.get(n) + 1
        
        pq = []   # priority queue
        res = []  # to store the result

        # build a min-heap
        for key,val in hm.items():
            heapq.heappush(pq, (val,key))
            if len(pq) > k:
                heapq.heappop(pq)
        
        while len(pq) > 0:
            res.append(heapq.heappop(pq)[1])
        return res
