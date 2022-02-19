class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''        
        As s and t consist of lowercase English letters, so we can solve this problem in 2 ways
            1. First approach: Create 2 lists of 26 length and compare them at the end, if they are same then the words are anagram.
            2. Second approach (better). Here we will use just one list of 26 length initialized to 0 values. 
                - For first char in first word increment the count for each char and for another char in second word, decrement the counter for each char.
                - If the counter at any character is < 0, it means that the word is not an anagram and thus return False. Else return True at end of second iteration
        '''
        
        # Using intutuion: lengths of both should words should be same
        if len(s) != len(t):
            return False
        
        # initialize the list of length 26 
        charList= [0]*26
        
        # loop over the first word and populate the charList 
        for i in s: 
            # increment the counter in first iteration
            charList[(ord(i)- ord('a'))] += 1  
        
        # loop over the second word to check if both words are same or not
        for i in t: 
            # decrement the counter for each character
            charList[(ord(i)- ord('a'))] -= 1  
            # if any count is less then 0 for the second word, it means both words are not unique
            if  charList[(ord(i)- ord('a'))] < 0:
                return False
        # return True in the end if words are found same
        return True 