class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        s = 0           # no of shifts that we will need for common prefix
        while (l < r):  # right shift by one unless both of the numbers are same
            l >>= 1
            r >>= 1
            s += 1
        return l << s  # now as `l` is common prefix, we need to shift it left for `s` number of times