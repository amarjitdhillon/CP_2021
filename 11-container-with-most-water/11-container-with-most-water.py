class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        - It's given that height.length > 2, so we do not need consider n == 1 case
        - As we want to find the max water, so initiaize l and r pointers at 0 and len(height)-1 resp
        - Set maxArea = 0
        - While l< r, compute maxArea with given l and r values
        - currArea = height * width = min(l,r) * (r-l+1)
        - if currArea  > maxArea, then update maxArea = currArea
        - return maxArea at end
        
        Time complexity: O(N) as both pointers will stop at l<r
        Space complexity = O(1) as vaiables are used which takes constant time
        '''
        maxArea, currArea, l, r = 0,0, 0, len(height)-1
        
        while(l < r and l >= 0 and r <= len(height)-1):
            currArea = min(height[l],height[r]) * (r-l)
            if currArea > maxArea:
                maxArea = currArea # udpate the max area
            
            if height[l] < height[r]: # left pointer needs to be incremented
                l += 1
            else:  # both cases of height[l] < height[r] and height[l] == height[r]
                r -= 1
        return maxArea
            
        