class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        - the idea is to place each number at it's right index
        - we can simply ignore the -ve elements
        - we can also ignore the out of bound elements, for example if len(arr) is 4 and val is 2000, so we can ignore that
        - we should swap the value to it's right index
        - at the end of the iteration, the first index to not have the value equal to it's index will be our answer
        '''
        for i in range(len(nums)):
            correctIdx = nums[i]-1
            # check if we can place the element
            while 0 <= correctIdx <= len(nums)-1 and nums[i] != nums[correctIdx]:
                # swap the values
                nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
                # update the correctIdx and do the swap operation again
                correctIdx = nums[i]-1
        
        # find out which number is misssing by doing a linear traversal   
        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        
        # handling the edge case when the array consists of all positive numbers. In that case we will return the next highest element which will be len(nums)+1
        return len(nums)+1
            