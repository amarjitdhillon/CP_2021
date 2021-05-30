
def findLongestSubs(word):
    s = 0
    e = 1
    max_dict = {}
    uniqueChars = set()
    word_len = len(word)
    maxLen = 0
    temp = '' # to save the local max string
    curr = ''
    while(e <= word_len):
        for i in range(s,word_len):
            curr = word[i]
            if word[i] not in uniqueChars:
                uniqueChars.add(curr)
                temp += str(curr)
                maxLen += 1 # as we have found a unique char
                e += 1 # increase the end
            else:
                # we need to increase the 's' so that repeating char is removed
                found = False
                wordi = ""
                words = ""
                while(not found):
                    wordi = word[i]
                    words = word[s]
                    if word[i] == word[s]:
                        uniqueChars.remove(word[s])
                        s += 1
                        found = True
                    else:
                        uniqueChars.remove(word[s])
                        s += 1

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
    return str(max_dict[key])



if __name__ == '__main__':
    # word = 'abcabcb'
    # word = 'bb'
    # word = "ABDEFGABEF"
    word = "GEEKSFORGEEKS" #EKSFORG
    # word = "CODINGISAWESOME" #NGISAWE

    print(findLongestSubs(word))