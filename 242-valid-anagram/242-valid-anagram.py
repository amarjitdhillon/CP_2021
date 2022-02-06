class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # as s and t consist of lowercase English letters, so we can solve this problem in 2 ways
            # 1. Create 2 list of 26 length and compare them at the end, if they are same --> words are anagram
            # 2. Second approach (better) is to use just one list of 0 values. For first word increment the count for each char and for another word decrement the counter for each char. If the counter at any character is < 0, it means that the word is not an anagram and thus return False. Else return True at end of second iteration
        
        # lengths of both should words should be same
        if len(s) != len(t):
            return False
        
        charList= [0]*26
        
        for i in s: 
            charList[(ord(i)- ord('a'))] += 1  # increment the counter in first iteration
        
        for i in t: 
            charList[(ord(i)- ord('a'))] -= 1  # decrement the counter in second iteration
            if  charList[(ord(i)- ord('a'))] < 0:
                return False
        
        return True 