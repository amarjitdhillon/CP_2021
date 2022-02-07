class Solution:
    """
    - As each char consists of lowercase English letters, so we can use the list of 26 lengths to represent each word
    - Loop over each word in the given input list
    - Create a hashmap of type {tuple: list}, where the key is a tuple of frequency count of length 26 representing each char of English alphabet and values is a list of anagrams for that tuple 
    - If two frequency tuples match, then append the current word to the end of this values list in the hashmap
    - f the tuple key is not present in the hashmap, then create a new key(tuple) and value pair (current word).
    - If the tuple key is present, then add the current word to the values list of the hashmap.
    - At the end, return the hashmap.values()
        """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        if len(strs) == 0:
            return []
        
        c_dict = {}
        
        for word in strs:
            freq_list = [0]*26
            
            for c in word:
                freq_list[ord(c)-ord('a')] += 1    # increment counter for freq in list
            
            freq_list = tuple(freq_list) # as tuple is immutable and can be used as key in dict
            
            if freq_list not in c_dict.keys():
                c_dict[freq_list] = [word]     # add the first word in the list
            else:
                c_dict[freq_list].append(word)  # add more anagrams to the list
                
        return c_dict.values()
        
        
        
        