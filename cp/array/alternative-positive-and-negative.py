"""
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2

---
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
"""
class Solution:
    def getPosAndNegative(self, arr):
        pl, nl = [], []
        for i in arr:
            if i < 0:
                nl.append(i)
            else:
                pl.append(i)
        pl = pl[::-1]
        nl = nl[::-1]
        sol = []
        while (len(pl) > 0) or len(nl) > 0:
            if len(pl) > 0:
                sol.append(pl.pop())
            if len(nl) > 0:
                sol.append(nl.pop())
        return sol

if __name__ == '__main__':
    arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
    # arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    obj = Solution()
    print(obj.getPosAndNegative(arr))
