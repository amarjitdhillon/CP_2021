'''
Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

'''
import operator
def sortByCharacters(arr):
    freq = {}
    for k in arr:
        if k not in freq.keys():
            freq[k] = 1
        else:
            freq[k] = freq.get(k)+1
    # print("freq =",freq)

    sfreq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    # print("sfreq",sfreq)

    ssfreq = {}
    for item in sfreq:
        k = item[1]
        v = item[0]
        if k not in ssfreq:
            ssfreq[k] = [v]
        else:
            temp = ssfreq.get(k)
            temp.append(v)
            ssfreq[k] = (sorted(temp, reverse=False))
    # print(ssfreq)

    # print the values
    result = []
    for k,v in ssfreq.items():
        for sv in v:
            for i in range(0,k):
                result.append(sv)

    return  result

if __name__ == '__main__':
    # arr = "tree"   #eetr
    # arr = "cccaaa" #aaaccc
    arr = "Aabb"   #bbAa

    out = sortByCharacters(arr)
    for i in out:
        print(i,end="")