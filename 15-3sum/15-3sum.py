class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        This can be done in 2 ways:
        1. without sorting, i.e modifying the original array
        2. with sorting, wo modifying original array
        """
        
        def withSorting(nums):
            """
            1. if len of the nums <=2, it means it does not have a triplet, so we can return []
            2. Else, sort the nums array
            3. loop over the list once form first till second last element, and set the low and high pointers
            4. set the low pointer as i+1 and high pointer as end of the list
            5. repeat till low < high
            6. if sum of three nums == 0 , add that element to the list, sort it and add them to a set (as we need to return the unique set)
            7. if the sum of three nums < 0, it means we need to move towards right, so decrement the high pointer
            8. if the sum of three nums > 0, it means we need to move towards left, so increment the low pointer
            """
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
                        result.add(tuple(sorted((nums[x],nums[b],nums[e]))))
                        
                        b += 1
                        e -= 1
                    if val < 0:
                        # we need to increase the result, so move towards the right side
                        b += 1
                    if val > 0:
                        e -= 1
            return result
            
        return withSorting(nums)
            
            
