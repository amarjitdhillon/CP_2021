# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.
# Example:
#
# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
# Output: 5
# Explanation: The missing number from 1 to 8 is 5

arr = {1, 2, 4, 5, 3, 7, 8, 9, 10}
n = 10

def missing(arr, n):
    expected_sum =  ((n)* (n+1))/2
    actual_sum = 0
    for i in arr:
        actual_sum += i
    diff = expected_sum-actual_sum

    if diff > 0:
        print(diff , "is the missing element")
    else:
        print("Nothing is missing")

missing(arr,n)

# if we use the sorting method, the time complexity will be O(nlogn), with sum method it is O(n)