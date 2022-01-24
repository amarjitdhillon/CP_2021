class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        This can be done in 2 ways:
        1. without sorting, i.e modifying the original array
        2. with sorting, wo modifying original array
        """
        
        def withSorting(nums):
            # special case
            if len(nums) <= 2:
                return []
            
            # result will contain the unique tuples
            result = set()
            
            nums = sorted(nums)
            
            for x in range(len(nums)-2):
                b = x+1
                e = len(nums)-1
        
                while b < e: # terminating condition
                    val = nums[x]+ nums[b] + nums[e]
                    if val == 0:
                        # we have found the sum
                        result.add(tuple(sorted([nums[x],nums[b],nums[e]])))
                        
                        b += 1
                        e -= 1
                    if val < 0:
                        # we need to increase the result, so move towards the right side
                        b += 1
                    if val > 0:
                        e -= 1
            return result
            
        return withSorting(nums)
            
            
