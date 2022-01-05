class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        
        # create a pascal triangle and later each row one by one
        pascal = []
        
        for x in range(n):
            # we will build a row first, the first row will be of size 1 and then 2, 3 4 etc
            row = [None for x in range(x+1)]
            
            # the first and last cols are always 1
            row[0], row[-1] = 1,1 
            
            # we have to modify the 1 to len(row)-1 rows using DP
            for y in range(1,len(row)-1):
                row[y] = pascal[x-1][y-1] + pascal[x-1][y]
            
            # append the row to triangle
            pascal.append(row)
        return pascal

                
        