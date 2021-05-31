"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = c
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000
"""

import math
def mergedMedian(n1,n2):
    l1 = len(n1)
    l2 = len(n2)
    if l1 < l2:
        a = n1
        b = n2
    else:
        a = n2
        b = n1


    # find the length of both the arrays
    la = len(a)
    lb = len(b)
    median = 0.0


    if la == 0:
        m = int(lb / 2)
        if lb%2 == 0:
            median = (b[m] + b[m-1])/2
        else:
            median = b[math.floor(m)]
        return median
    elif lb == 0:
        y = int(la/2)
        if la%2 == 0:
            median = (a[y] + a[y-1])/2
        else:
            median = a[math.floor(y)]
        return median


    # we will use the low and high to find the cut for both the arrays
    low  = 0
    high = la # we will do the binary search on the smallest array

    while(high >= low):
        ca = int((low + high)/2)
        cb = int(((la + lb +1)/2) - ca)

        # al and ah are low and high for first array(a)
        al = a[ca-1] if ca > 0 else -math.inf
        ah = a[ca] if ca < la else math.inf
        bl = b[cb-1] if cb > 0 else -math.inf
        bh = b[cb] if cb < lb else math.inf

        if (al <= bh) and (bl <= ah):
            # then we have found the perfect cut, so now we need to see how to find the median
            if (la+lb)%2 == 0:
                median = (max(al,bl) + min(ah,bh))/2
            else:
                # means the median is in first half as first half will have the more number of elements
                median = max(al,bl)
            return median
        elif bl > ah:
            # we need to move towards right by increasing the value of low.
            # Note that the value of high is already max, so we don't want to change it
            low = ca+1
        else:
            # we need to move towards left which means that we will change the high values
            # Note that the value of low is alredy lowest, i.e zero
            high = ca-1
    return median

if __name__ == '__main__':
    # nums1 = [1,2]
    # nums2 = [4,5,6] # 2.50000

    # nums1 = [1,2,3]
    # nums2 = [5,6] # 2.50000

    # nums1 = [1,2,3]
    # nums2 = [5,6,7] # 2.50000

    # nums1 = [0, 0]
    # nums2 = [0, 0] # 0.0000
    #
    # nums1 = []
    # nums2 = [1] # 1.0000
    #
    # nums1 = [1]
    # nums2 = [2,3] # 2.00000

    # nums1 = []
    # nums2 = [2,3] # 2.50000

    nums1 =  [1]
    nums2 = [2, 3, 4]
    print(mergedMedian(nums1,nums2))
