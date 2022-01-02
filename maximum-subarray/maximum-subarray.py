class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        The logic used here is that, as we want to find the continuous max sum, so we will reject the sum if it's < 0
        Also, we will update the max result found so far in a variable at every step
        '''
        
        local_sum, max_subarray = 0, nums[0]
        for x in nums:
            local_sum += x
            
            # the local sum can be less than 0 and it still can be a max sum in the subarray
            # That is why we need to check this condition here first
            if local_sum > max_subarray:
                max_subarray = local_sum
                
            # reset if sum is negative
            if local_sum < 0: 
                local_sum = 0

        return max_subarray
                    
