"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""


def findRainWater(arr):
    la = len(arr)
    water = 0

    if la <= 2:
        return water

    leftMax = arr[0]
    rightMax = arr[la-1]

    leftMaxArr = [0 for i in range(la)]
    rightMaxArr = [0 for i in range(la)]

    # find the left max
    for i in range(1, la):
        prev = arr[i-1]
        if prev > leftMax:
            leftMax = prev
        leftMaxArr[i] = leftMax

    # find the right max array
    for i in range(la-2,-1,-1):
        prev = arr[i+1]
        if prev > rightMax:
            rightMax = prev
        rightMaxArr[i] = rightMax

    width = 1
    for i in range(1,la-1):
        waterLevel = min(leftMaxArr[i],rightMaxArr[i])
        if waterLevel-arr[i] > 0:
            water += (waterLevel-arr[i]) * width

    return water

if __name__ == '__main__':
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] #6
    height = [4,2,0,6,2,3,5] #9


    print(findRainWater(height))