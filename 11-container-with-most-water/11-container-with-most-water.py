class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
            - It's given that height.length > 2, so we do not need consider n == 1 case
            - As we want to find the max water area, so initialize l and r pointers at 0 and length(height)-1 respectively- 
            - Width between 2 consecutive nums = 1
            - Set maxArea = 0 initially
            - While l< r and (l and r are in bounds), compute currArea with given l and r values. 
            - Here currArea represents currentArea given l and r as pointers holding water.
            - currArea = height * width = min(height[l],height[r]) * (r-l)
            - If currArea > maxArea, then update maxArea = currArea
            - return maxArea at the end
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
            
        