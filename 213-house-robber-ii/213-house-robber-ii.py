class Solution:
    def rob(self, nums: List[int]) -> int:
        # we don't need to consider len(nums) = [0,1] as 1 <= nums.length <= 100
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # function to rob a neighbourhood in a straight line
        def robHouse(houses) -> int:
            prevRob, SecondPrevRob, currRob = 0, 0, 0
            
            # lets rob all the houses
            for h in houses:
                currRob         = max(h+SecondPrevRob, prevRob)
                
                # update values for next iteration
                SecondPrevRob   = prevRob
                prevRob         = currRob
                
            # at the end of iteration, the prevRob was updated to currRob, so we can return either of these
            return currRob      
        
        '''
        If we choose to rob first house (0 index) then we can't rob the last one as both are connected, so it means we can rob from 0 to N-1. In Python slicing [0:N] means N is not included. 
        iIf we choose NOT to rob the first house, then we can rob from 1 to N
        The final result will be max of both of these robs
        '''
        N = len(nums)-1       
        return max(robHouse(nums[0:N]) , robHouse(nums[1:]) )
