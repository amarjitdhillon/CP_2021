class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        t, b ,l, r = 0, len(mat), 0, len(mat[0])    # define top, bottom, left and right
        res = []                                    # final result array
        
        while((l < r) and (t < b)):             # print till the bounds don't collide 
            
            for i in range(l, r):               # print the top row, left to right from l to r
                res.append(mat[t][i])
            t += 1
            
            for i in range(t, b):               # print the right row, top to bottom form t to b(excluded)
                res.append(mat[i][r-1])
            r -= 1
            
            if l == r or t == b:                # break condition
                return res
            
            for i in range(r-1, l-1, -1):       # print bottom row in reverse from right to left. 
                res.append(mat[b-1][i])
            b -= 1
               
            for i in range(b-1, t-1, -1):       # print the left row from bottom to top
                res.append(mat[i][l])
            l += 1     
        return res
        
        
        