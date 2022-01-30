class Solution:
    def findComplement(self, num: int) -> int:
        '''
        The solution is tricky for this questions. Let's take an example:
        1010 is the input which will result in 0101 that can be written as (0 * 2^3) + (1 * 2^2) +(0 * 2^1) +(1 * 2^0)
        0101 be written as   (1 * 2^2) +(1 * 2^0)
		Steps:
			run a loop till nums > 0
            if the last bit in nums is 0
				if yes, then we need to flip it to 1 and get it's actual value in terms on 2^x, We can do so by using bit right shift operator of 1 << x, where x is the interation number
				Add this value to the result
			We do not need to do anything if last value is 1 (nums&1 == 1) in nums as it will be flipped to 0 in it's complement 
			Right shift the nums by one to process the next bit
			Increment the iteration counter (x)
        '''
        r = 0
        x = 0                   # x will give the value as 2^x for each bit
        
        while(num > 0):         # we will stop when it becomes 0 as it's the min value num can be
            last_bit = num&1
            if last_bit == 0:   #then we need to convert it to 1 and get it's original value
                value = 1<<x
                r += value
            num >>= 1           # after operation is done for the last bit, we will right shift num by one to process next bit
            x += 1
        return r
