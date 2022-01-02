from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' In this case we are using the 2 pass hashmap scheme. In the first pass every element is added as key and it's index is added as a value. For the second pass, we will check if the complement of this element exists in tehe hahmap, if it does then we will return the index of the element and it's complement '''
        # first pass
        nums_hashmap = defaultdict(list)
        for x in range(len(nums)):
            nums_hashmap[nums[x]] = x
        
        # second pass
        for y in range(len(nums)):
            complement = target - nums[y]
            if complement in nums_hashmap and nums_hashmap[complement] != y:
                return [y, nums_hashmap[complement]]
            
