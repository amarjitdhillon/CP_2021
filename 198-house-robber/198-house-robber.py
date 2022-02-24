class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: one house
        if len(nums) == 1:
            return nums[0]
        
        rob1, rob2 = 0, 0
        for rob in nums:
            curr = max(rob1+ rob, rob2)
            rob1 = rob2
            rob2 = curr
        return rob2