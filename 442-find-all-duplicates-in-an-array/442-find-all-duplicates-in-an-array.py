class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r = []                       # will hold the result array
        for x in nums:
            if nums[abs(x)-1] < 0:   # if element the the target index is -ve then it means we have already reached there
                r.append(abs(x))
            nums[abs(x)-1] *= -1     # mark the location as -ve
        return r
            
        