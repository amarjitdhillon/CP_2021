"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestPrefix(s):
    sl = len(s)

    if sl == 0:
        return ""

    if sl == 1:
        return str(s[0])

    prefix = ""
    i = 0           # this is used to denote which char are we picking, we will start from zeroth
    first = s[0]    # save the first word as reference
    lenFirst = len(first)

    if lenFirst == 0:
        return prefix

    for x in range(lenFirst):
        for w in range(1,len(s)): # we are iterating from second word onwards

            if s[w] == "": # if word is empty then we will return
                return prefix


            wordLen = len(s[w])

            # it is possible that value of i gets higher then the max chars in word
            if i > wordLen-1 or i > lenFirst-1:
                return prefix
            word = s[w]
            char = s[w][i] # get the char in the word which we want to check


            if char != first[i]:
                break

            if w == len(s)-1:       # then this is the last word in the list
                prefix += char      # save this char to prefix
                i += 1              # incrementing as we need to check the next char

    return prefix if len(prefix) > 0 else ""

if __name__ == '__main__':
    # s = ["flower", "flow", "flight"]
    # s = ["dog","racecar","car"]
    # s = ["",""]
    s = ["flower", "flower","flower"]
    s = ["ab","a"]


    print(longestPrefix(s))