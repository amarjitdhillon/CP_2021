class Solution:
    def findComplement(self, num: int) -> int:
        '''
        The solution is tricky for this questions. Let's take an example:
        1010 will result in 0101 ( (0 * 2^3) + (1 * 2^2) +(0 * 2^1) +(1 * 2^0))
        01001 is equal to  0101 ( (1 * 2^2) +(1 * 2^0))
        Now all we need to do it to find if the last bit in nums is 0
            if yes, then we need to flip it to 1 and get it's actual value in terms on 2^x
            We can do so by using bit right shift operator of 1 << x, where x is the interation number
        '''
        r = 0
        i = 0                   # i will give the value as 2^i for each bit
        
        while(num > 0):         # we will stop when it becomes 0 as it's the min value num can be
            last_bit = num&1
            if last_bit == 0:   #then we need to convert it to 1 and get it's original value
                value = 1<<i
                r += value
            num >>= 1           # after operation is done for the last bit, we will right shift num by one to process next bit
            i += 1
        return r
        