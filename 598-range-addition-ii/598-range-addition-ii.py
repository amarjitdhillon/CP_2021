class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for r,c in ops:
            # expand and shrink the matrix size (bottom-right boundry of matrix) based on the current operation
            m = min(m,r)
            n = min(c,n)
        # total number of elements will be multiplication of bottom and right boundry asssming left and top boundry is 0,0
        return m*n
        