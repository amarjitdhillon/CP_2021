
"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

def increment( arr, N):
    inc = True
    for i in range(len(arr) - 1, -1, -1):
        if inc:
            if (arr[i] == 9):
                if i == 0:              # means this is the last element
                    arr[i] = 0
                    temp = ""
                    for i in arr:
                        temp += str(i)
                    arr = list(temp + "1")
                    return arr[::-1]
                else:
                    arr[i] = 0
            else:
                arr[i] += 1
                inc = False
    return arr


if __name__ == '__main__':
    # arr = [9, 9, 9, 9]
    # arr = [9, 8, 9]
    # arr = [0, 9]
    # arr = [0,0,8, 9]
    arr = [ 9]
    N = len(arr)

    res = increment(arr,N)
    for i in res:
        print(i, end=" ")