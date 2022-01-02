from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = defaultdict(list)
        for x in range(len(nums)):
            nums_hashmap[nums[x]] = x
        
        for y in range(len(nums)):
            complement = target - nums[y]
            if complement in nums_hashmap and nums_hashmap[complement] != y:
                return [y, nums_hashmap[complement]]
            
