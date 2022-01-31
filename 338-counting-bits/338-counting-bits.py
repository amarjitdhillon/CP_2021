class Solution:
    def countBits(self, n: int) -> List[int]:
        r = [0] * (n+1)
        for x in range(1,n+1):
            r[x] = r[x//2] + x%2   # P(x)=P(x/2)+(xmod2)
        return r
        