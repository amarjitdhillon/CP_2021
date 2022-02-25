"""
Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G
  B   D   F   H
Now concatenate the two rows and ignore spaces
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
"""
def zigzag(s, rows):
    res = [[] for i in range(rows)] # we will store the result here

    r = 0
    dir = -1 # we are taking the direction as negative/upwards here, as we will flip it first time
    val = ""     # we will store the result in this string

    # edge case when the rows == 1, so we can return the same string
    if rows ==1:
        return s

    for c in s:
        res[r] += c
        if r == rows-1 or r == 0: # we need to flip the side if we reached the top or bottom list
            dir = -dir
        r = r+dir

    # logic to make the resulting string to print to output
    for i in res:
        for c in i:
            val += str(c)
    return val

if __name__ == '__main__':
    # s = "geeksforgeeks"
    s = "abcdefgh"
    s = "PAYPALISHIRING"
    s = "AB"
    rows = 1
    print(zigzag(s,rows))