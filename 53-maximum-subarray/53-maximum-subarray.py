class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        The logic used here is that, as we want to find the continuous max sum, so we will reject the all values to the left if the sum < 0
        Also, we will update the max result found so far in a variable at every step
        At the end, return max result
        '''
        
        # add first element as the max_sum as len(nums) > 1 ( as per given constaint)
        current_sum, max_sum = 0, nums[0] 
        
        for x in nums:
            current_sum += x
        
            # update the max sum
            if current_sum > max_sum:
                max_sum = current_sum
                
            # reset the current sum if it is negative
            if current_sum < 0: 
                current_sum = 0

        return max_sum
                    
