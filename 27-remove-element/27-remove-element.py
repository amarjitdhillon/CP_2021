class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # update the pivot element with the current element
                nums[pivot] = nums[i]
                # update pivot as this element is updated
                pivot += 1
        # pivot pointer is what is being asked form us to return
        return pivot
                