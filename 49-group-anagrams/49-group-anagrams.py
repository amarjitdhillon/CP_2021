class Solution:
    """
    - As each char consists of lowercase English letters,so we can use the list of 26 lengh to represent each word
    - Create a hashmap of type list:list, where key is list of lengh 26 frequency count and values is a list of word which match that freq count 
    - If two lists match, then append the word to the end of this values list in hashmap
    - If that key of list is not present in the hashmap, then create a new key and value pair.
    - At the end, append the list values of hashmap to result list and return result list
        """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        if len(strs) == 0:
            return []
        
        c_dict = {}
        
        for word in strs:
            freq_list = [0]*26
            
            for c in word:
                freq_list[ord(c)-ord('a')] += 1   
                
            if tuple(freq_list) not in c_dict.keys():
                c_dict[tuple(freq_list)] = [word]
            else:
                c_dict[tuple(freq_list)].append(word)
                
        return c_dict.values()
        
        
        
        