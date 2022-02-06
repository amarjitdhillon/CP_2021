class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # as s and t consist of lowercase English letters, so we can create an array of lengh 26 represendng each char
        charListS, charListT = [0]*26, [0]*26
        
        for i in s:
            charListS[(ord(i)- ord('a'))] += 1
        
        for i in t:
            charListT[(ord(i)- ord('a'))] += 1
        
        return True if charListS == charListT else False