class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        """
        We can use the 2 pointer technique here
        """
        # sort the list first
        nums = sorted(nums)
        
        result, diff = 0, math.inf
        
        for p in range(len(nums)-2):
            l = p+1
            h = len(nums)-1
            
            while l < h: # break condition for 2 pointers
                x = nums[p] + nums[l] + nums[h]
                if x < t:
                    l += 1
                elif x > t:
                    h -= 1
                elif abs(x - t) == 0:
                    return x # returning as we have found the value
                
                # update diff if it has high value then current difference we found 
                if abs(x - t) < diff:
                    diff = abs(x - t)
                    result = x
                    
        return result
            
                
                    