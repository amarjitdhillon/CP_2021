class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        if the # of 2 in `n` is one then it's a power of 2
        '''
        c = 0 # count
        while(n > 0):
            if n&1 == 1:
                c += 1
            n >>= 1
        return True if c == 1 else False