
def findLongestSubs(word):
    s = 0
    e = 1
    max_dict = {}
    uniqueChars = set()
    word_len = len(word)
    maxLen = 0
    temp = '' # to save the local max string
    curr = ''
    end = False

    # checking the edge case
    if word == "":
        return 0

    while(not end):
        for i in range(s,word_len):
            curr = word[i]
            if i >= word_len-1:
                end = True
            if word[i] not in uniqueChars:
                uniqueChars.add(curr)
                temp += str(curr)
                maxLen += 1 # as we have found a unique char
                e += 1 # increase the end
            else:
                # we need to increase the 's' so that repeating char is removed
                found = False

                while(not found):
                    if  word[s] == word[i]:
                        s += 1
                        found = True
                    else:
                        s += 1
                uniqueChars.clear()
                # we have found the repeating char
                # saving the temp string
                if maxLen > 0:
                    if(maxLen in max_dict.keys()):
                        t = max_dict[maxLen]
                        t.append(temp)
                        max_dict[maxLen] = t
                    else:
                        max_dict[maxLen] = [temp]
                maxLen = 0
                temp = ''
                break

    if e >= word_len:
        if maxLen > 0:
            if (maxLen in max_dict.keys()):
                t = list(max_dict[maxLen])
                t.append(temp)
                max_dict[maxLen] = t
            else:
                max_dict[maxLen] = [temp]
    print(max_dict)
    key = max(max_dict.keys())
    return key


if __name__ == '__main__':
    # word = 'abcabcb'
    # word = 'bb'
    # word = "ABDEFGABEF" # ABDEFG || 6
    # word = "GEEKSFORGEEKS" #EKSFORG || 7
    # word = "CODINGISAWESOME" #NGISAWE || 7
    # word = "abcabcbb" # abc
    # word = "pwwkew" # wke
    # word = ""
    word = "dvdf" # vdf/3
    # word = "bpfbhmipx"
    # word = "ab"


    print(findLongestSubs(word))