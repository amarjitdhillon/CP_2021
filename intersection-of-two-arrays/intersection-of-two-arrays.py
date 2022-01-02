class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. put the both lists to set to get the unique valeus 
        # 2. find the common values from both sets by iterating over the smaller set and finding the values which exists in both sets
        # 3. return the common values
        
        s1 = set(nums1)
        s2 = set(nums2)
        
        def find_intersection(set_a, set_b):
            res = []
            # here seta is the smaller set
            for val in set_a:
                if val in set_b:
                    res.append(val)
            return res
        
        if len(s1) < len(s2):
            return find_intersection(s1,s2)
        else:
            return find_intersection(s2,s1)
            

            
        