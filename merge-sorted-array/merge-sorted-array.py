class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we will take 3 pointers, x ,y and z
        x,y,z  = m-1,n-1,m+n-1
        while (x > -2) and (y> -1):
            if y< 0:
                break
            if x >=0 and (nums2[y] < nums1[x]):
                nums1[z] = nums1[x]
                # update the x pointer as x value is copied
                x -= 1
            else:
                nums1[z] = nums2[y]
                # update the y pointer as y index value is copied
                y -= 1
            z -= 1 # decrement the pointer in either of the case
        return nums1