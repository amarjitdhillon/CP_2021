"""
Given a string, find the longest substring which is palindrome.

For example,
Input: Given string :"forgeeksskeegfor",
Output: "geeksskeeg"

Input: Given string :"Geeks",
Output: "ee"
"""

def longestPalindrome(a):
    la = len(a)

    # if string is empty
    if la == 0:
        return "string is empty"

    # if there is just one char
    if la == 1 :
        return a[0]

    # if there are 2 chars and they are different
    if la ==2 and a[0] != a[1]:
        return a[0]

    pd = {} # palindrome dictionary
    lp = 0 # length of palindrome
    temp = ""

    # handling the case if the length of palindrome is odd
    for i in range(1,la-1): # we are going to the second last char as we need to see the prev and next element
        prev = a[i-1]
        curr = a[i]
        next = a[i+1]

        if prev == next:
            lp = 3
            temp = str(prev)+str(curr)+str(next)
            p = i-2
            n = i+2
            while(p >= 0 and n<=(la-1)):
                prev = a[p]
                next = a[n]
                if prev == next: # means both the elements on the left and right are same
                    p -= 1
                    n += 1
                    temp = str(prev)+temp+str(next)
                    lp += 2
                else:
                    break

        # now we need to save the palindrome that we found
        if lp > 0:
            if lp not in pd.keys() and temp != "":
                pd[lp] = [temp]
            else:
                t = pd[lp]
                t.append(temp)
                pd[lp] = t

   # when palindrome is even
    for i in range(0,la-1):
        curr = a[i]
        next = a[i+1]
        temp = ""
        if next == curr:
            # Then we need to check logic for the palindrome
            p = i-1
            n = i+2
            temp = str(curr)+str(next)
            lp = 2
            while(p >= 0 and n<=la-1):
                prev = a[p]
                next = a[n]
                if prev == next:
                    p -= 1
                    n += 1
                    temp = prev+temp+next
                    lp += 2
                else:
                    break

        # now we need to save the palindrome that we found
        if lp > 0 and temp != "":
            if lp not in pd.keys():
                pd[lp] = [temp]
            else:
                t = pd[lp]
                t.append(temp)
                pd[lp] = t

    if len(pd.keys()) > 0:
        max_key = max(pd.keys())
        return pd[max_key][0]
    else:
        return a[0]


if __name__ == '__main__':
    # s = "ababa"
    # s = "Geeks"
    s = "babad" #bab
    s = "cbbd" #bb
    s = "a"  #a
    s = "cbbd"
    s = "bb"
    s = "aaaa" #aaaa
    print(longestPalindrome(s))