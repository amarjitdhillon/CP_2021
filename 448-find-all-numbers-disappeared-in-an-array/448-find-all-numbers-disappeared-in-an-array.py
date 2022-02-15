class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setA = set(nums)
        setB = {i for i in range(1,len(nums)+1)}
        return(setB - setA)