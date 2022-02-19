class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # We will right shift the digits by one and increase the counter if the `bitwise-and` of this number is 1
        # This operation will be done unless the value is > 0
        while(n > 0):
            # if the `bitwise-and` with digit 1 is 1, it means that the last bit is one, so we will increase the counter
            if n&1 == 1:   
                count += 1
         # right shift by one digit, to process the next bit in the next iteration
            n >>= 1        
        return count
