class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Brute force method
        - create a merged array 
        - sort that merged array
        - find the median based on length of merged array
        
        TC: m+n+ (m+n) = O(m+n)
        SC: O(m+n)
        """
            
        """
        Optimized solution steps:
        - Make sure x is the smaller list as we want to reduce the complexity for binary serach
        - initiate the low and high for x list
        - Find partition for first list (X) using the mid value of low and high
        - Find partition of the second list using mid- partitionX - 2 (we used 2 here as both list are 0 based)
        - populate the xmin based on partition we found, if the partition index is lesser then 0, then we will initiaize the value to -infinity.
            We need -inf as we need something to compare. 
            We checked the lower bound only we want to find the min value
        - likewise, we will the xmax based on partition we found, if the partition index grater then length of list, then we will initiaize the value to +infinity.
        - Populate ymin and ymax too
        - We know that xmin in less then xmax and ymin is less then ymax (as the array is sorted), Now if xmin < ymax and ymin < xmax it means we have found the right partition
            - As we have found the partition, we we can find the median based on if the total number in both lists are odd or even
            - if the sum is even, it means we need to take max value from left lists and min value from right lists. Both of these values will be adjoining one another if we would have merged both lists.
                - Now as we have the 2 middle values, we can find the median by taking average
            - if the sum is odd, then we will have one extra element in the right part of the list, bases on the `cy = mid -cx - 2` formula we used, so to find the median in this case we will take the min value of the right side lists
        - if the xmin > ymax, then we have not found the partition. Also, as the xmin is greater, so we want to make it smaller. Means we are looking for a smaller value in the binary serach, so just update the high pointer to cx(mid) -1
        - Else, update the low pointer to cx (mid) +1
        
        TC: max O(log(m+n))
        SC: O(1)
        """
        x,y = nums1, nums2
        
        if len(x) > len(y):
            x, y = y, x
        
        lx, ly = len(x), len(y)
            
        l,h = 0, lx-1
        mid = (lx + ly) // 2

        while True:
            cx = (h+l)//2      # using binary search
            cy = mid -cx - 2   # because of 0 based indexing of both arrays

            xmin = x[cx] if cx >= 0 else - math.inf
            xmax = x[cx+1]  if cx+1 < lx else math.inf
            ymin = y[cy] if cy >= 0 else - math.inf
            ymax = y[cy+1] if cy+1 < ly else  math.inf

            if xmin <= ymax and ymin <= xmax: #as xmin is already less than xmax and ymin in already less then ymax
                if (lx+ly) % 2 == 0: # even case
                    return (max(xmin,ymin) + min(xmax,ymax))/2
                else:
                    return min(xmax , ymax)
            elif xmin > ymax:
                # we need to move the cut to left hand side as xmin is still bigger
                h = cx -1
            else:
                l = cx+1
