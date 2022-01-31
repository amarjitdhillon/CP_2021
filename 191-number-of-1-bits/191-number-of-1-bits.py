class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n > 0):
            if n&1 == 1:   #means the last bit is one, so increase the counter
                count += 1
            n >>= 1         # right shift by one, to process the next bit
        return count
