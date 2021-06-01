"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
"""

def maxArea(height):

    lh = len(h)

    if lh == 0:
        return 0 # 0 area as there is no element

    if lh == 1:
        return h[0] # returning the first element of the height array

    # create the points in x,y form
    p = [0 for i in range(lh)]
    i = 0
    for val in h:
        p[i] = [i+1, val]
        i += 1
    print(p)

    left = 0  # we are using the 2 pointer scheme where left represents the leftmost and right is the rightmost pointer
    right = lh-1
    result = [] # this will store the result areas from which we will consider one with the max value
    area = 0

    # area = (x2-x1)*min(y1,y2) This is the formula that we will use to compute the area

    while(left < right):
        area = (p[right][0] - p[left][0]) * min(p[right][1], p[left][1])
        result.append(area) # save the area

        if p[left][1] < p[right][1]:
            left += 1 # we will move the left as it is smaller
        else:
            right -= 1 # move the right pointer to left
    return max(result)

if __name__ == '__main__':
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7] #49
    # h = [1,1] #1
    # h = [4,3,2,1,4] #16
    # h = [1,2,1] #2
    # h = [2,3,4,5,18,17,6] # 17
    print(maxArea(h))