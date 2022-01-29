class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: # special case
            return 0
        
        slow = fast = nums[0]
        
        for x in range(len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        fast = nums[0]
        while(fast != slow):
            fast = nums[fast]
            slow = nums[slow]
            
        return slow
        