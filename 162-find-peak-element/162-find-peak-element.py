class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        while(l < r):
            m = (l+r)//2
            if nums[m] > nums[m+1]: # peak is at left for sure, so update the r pointer
                r = m
            else : # peak is at right for sure, so update l pointer
                l = m+1
        return l
            
                
        