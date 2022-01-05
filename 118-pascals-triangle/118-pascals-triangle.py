class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        # if n == 1:
        #     return [1]
        
        
        # create a pascal triangle
        pascal = []
        
        for x in range(n):
            row = ["X" for x in range(x+1)]
            row[0], row[-1] = 1,1 
            
            for y in range(1,len(row)-1):
                row[y] = pascal[x-1][y-1] + pascal[x-1][y]
            
            pascal.append(row)
        print(pascal)
        return pascal

                
        