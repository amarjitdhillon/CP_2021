from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        This hashmap algo is based on 2 steps.
        1. In step one we will go through the smaller list and create a frequency map of the items
        2. In step two, we will linearly iterate over the second list, if the item is in the freq map then we will reduce the count in freq map and add this value to a result array
        3. Return the result array
        '''
        def create_frequency_map(nums_s):
            for x in nums_s:
                fm[x] = fm[x] + 1
                    
        def find_intersection(nums_l):
            for y in nums_l:
                if y in fm and fm[y] > 0:
                    # reduce the count in frequency map
                    fm[y] = fm[y] -1
                    result.append(y)
            return result
        
        fm = defaultdict(int)
        result = []
        
        if len(nums1) >= len(nums2):
            create_frequency_map(nums1)
            return find_intersection(nums2)
        else:
            create_frequency_map(nums2)
            return find_intersection(nums1)

        '''
        Time complexity: O(m+n) as we are going through both of the lists once
        Space complexity: 2* O(min(m,n)) for hashmap and result array
        '''
            
        
        