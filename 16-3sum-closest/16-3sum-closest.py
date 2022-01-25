class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        """
        We can use the 2 pointer technique here
        """
        # sort the list
        nums = sorted(nums)
        result = 0
        diff = math.inf
        
        for p in range(len(nums)-2):
            l = p+1
            h = len(nums)-1
            
            while l < h:
                x = nums[p] + nums[l]+nums[h]
                if x < t:
                    l += 1
                elif x > t:
                    h -= 1
                elif abs(x - t) == 0:
                    return x
                
                # update diff if it has low value
                if diff > abs(x - t):
                    diff = abs(x - t)
                    result = x
                    
        return result
            
                
                    