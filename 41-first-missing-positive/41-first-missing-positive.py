class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        - The idea is to place each number at it's right index.
        - We can simply ignore the -ve elements.
        - We can also ignore the out of bound elements, for example if len(arr) is 4 and val is 2000, so we can ignore that.
        - We should swap the value to it's correct index (eqal to it's value is that value is in bound ofl length of nums).
        - At the end of the iteration, the first index to not have the value equal to it's index will be our answer.
        '''
        for i in range(len(nums)):
            correctIdx = nums[i]-1
            # Check if we can place the element
            while 0 <= correctIdx <= len(nums)-1 and nums[i] != nums[correctIdx]:
                # Swap the values
                nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
                # Update the correctIdx and do the swap operation again
                correctIdx = nums[i]-1
        
        # Find out which number is misssing by doing a linear traversal   
        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        
        # Handling the edge case when the array consists of all positive numbers. In that case we will return the next highest element which will be len(nums)+1
        return len(nums)+1
            