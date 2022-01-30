class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        if ^ means the xor operation, then we need to know that 
        x ^ x = 0
        x ^ 0 = x
        """
        
        # first, we take the overall xor for this range and save in r
        r = 0
        for x in range(len(nums)+1): # len(nums) gives the total no of elements and +1 to include that number
            r ^= x
        
        # XOR tthe result of overall XOR with all numbers
        for y in nums:
            r ^= y 
        return r
            
        