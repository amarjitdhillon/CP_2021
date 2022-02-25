'''
1636. Sort Array by Increasing Frequency (Leetcode)

Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
'''
import operator

def freqArray(arr):
    freq = {}
    for i in arr:
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1

    # sort it using the frequency as a tuple
    s_freq = sorted(freq.items(), key=operator.itemgetter(1))
    # print(s_freq)

    ss_freq = {}
    # ss_freq represents the sorted dict where key is the frequency and value is the items which are repeating
    # Also, the values are sorted in decreasing order
    for x in range(0,len(s_freq)):
        skey = s_freq[x][1]
        sval = s_freq[x][0]
        if skey not in ss_freq:
            ss_freq[skey] = [sval]
        else:
            temp = []
            pval = ss_freq.get(skey)    # this will be a list as we are adding values as list
            for x in pval:
                temp.append(x)          # add all the values in the k,v pair
            temp.append(sval)           # add the current value to temp list
            temp = sorted(temp, reverse=True)
            ss_freq[skey] = temp

    # print the results
    s_result = []
    for k,v in ss_freq.items():
        for val in v:
            for i in range(0,k):
                s_result.append(val)
    return s_result

if __name__ == '__main__':
    # arr = [1,1,2,2,2,3]           # [3, 1, 1, 2, 2, 2]
    # arr = [2,3,1,3,2]               # [1, 3, 3, 2, 2]
    arr = [8, -8, 2, -8, -5, -3]  # [8, 2, -3, -5, -8, -8]
    print(freqArray(arr))