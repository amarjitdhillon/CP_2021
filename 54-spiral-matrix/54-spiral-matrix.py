class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        t, b ,l, r = 0, len(mat), 0, len(mat[0])
        res = [] # final result array
        
        while((l < r) and (t < b)):
            # print the top row
            for i in range(l, r):
                res.append(mat[t][i])
            t += 1
            
            # print the right row
            for i in range(t, b):
                res.append(mat[i][r-1])
            r -= 1
            
            if l == r or t == b:
                return res
            
            # print bottom row
            for i in range(r-1, l-1, -1):
                res.append(mat[b-1][i])
            b -= 1
            
            # print the left row
            for i in range(b-1, t-1, -1):
                res.append(mat[i][l])
            l += 1
            
        return res
        
        
        