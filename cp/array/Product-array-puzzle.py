# https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1

'''
Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
'''

def productArray(arr):
    N = len(arr)
    if N == 1 or N == 0:
        return 0

    pre = [1 for i in arr]
    for i in range(1, len(arr)):
        pre[i] = pre[i-1] * arr[i-1]

    post = [1 for i in arr]
    for i in range(len(arr)-2,-1, -1):
        post[i] = post[i+1] * arr[i+1]

    sol = [1 for i in arr]
    for i in range(0,len(arr)):
        sol[i] = pre[i]* post[i]

    return sol


# arr = [2, 3, 4, 5]
# arr = [2]
arr = []
print(productArray(arr))