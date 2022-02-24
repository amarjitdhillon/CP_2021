class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: one house
        if len(nums) == 1:
            return nums[0]
        
        secondLastRob, lastRob = 0, 0
        for rob in nums:
            # our current rob can include current house + all houses excluding last rob OR the last robbed values as we are excluding the current rob
            currRob         = max(secondLastRob+rob, lastRob)
            # update the last robbed sum for next iteration
            secondLastRob   = lastRob
            # update the last rob sum for next iteration
            lastRob         = currRob
        return lastRob                      # as the lastRob was updated to currRob at the end of the iteration