class Solution:
    def generate(self, n: int) -> List[List[int]]:
        # edge case scenario
        if n == 0:
            return []

        # create a pascal triangle and then add each row one by one to it
        pascal = []
        
        for x in range(n):
            # we will build a row first. The first row will be of size 1 and later will be of size 2, 3, 4 etc
            row = [None for _ in range(x+1)]
            
            # the first and last cols are always 1 for any given row
            row[0], row[-1] = 1, 1 
            
            # we have to update the values from index 1 to len(row)-1 using DP such that the current val is sum of two previous elements from upper row
            for y in range(1,len(row)-1):
                # here the values for row are taken from the pascal triangle. Both of these values are from one row above (using `x-1` here)
                row[y] = pascal[x-1][y-1] + pascal[x-1][y]
            
            # append the row to triangle
            pascal.append(row)
        return pascal

                
        