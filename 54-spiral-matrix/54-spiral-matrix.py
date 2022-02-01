class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        t, b ,l, r = 0, len(mat), 0, len(mat[0])
        res = []                            # final result array
        
        while((l < r) and (t < b)):   
            for i in range(l, r):           # print the top row
                res.append(mat[t][i])
            t += 1
            
            for i in range(t, b):           # print the right row
                res.append(mat[i][r-1])
            r -= 1
            
            if l == r or t == b:            # break condition
                return res
            
            for i in range(r-1, l-1, -1):   # print bottom row
                res.append(mat[b-1][i])
            b -= 1
               
            for i in range(b-1, t-1, -1):   # print the left row
                res.append(mat[i][l])
            l += 1     
        return res
        
        
        