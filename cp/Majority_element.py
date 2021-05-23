# When an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an
# element that appears more than N/2 times in the array.

def majorityElement(A):
    # Your code here
    bl = len(A) // 2
    dic = {}
    if len(A) == 1:
        return A[0]
    for i in A:
        if i not in dic.keys():
            dic[i] = 0
        else:
            dic[i] += 1
            if dic[i] >= bl:
                return i
    return -1

if __name__ == '__main__':
    A = [1,3,3,2,3]
    N = len(A)
    print(majorityElement(A))