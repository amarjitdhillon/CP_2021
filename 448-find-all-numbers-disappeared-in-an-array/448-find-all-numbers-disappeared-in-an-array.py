class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # convert the nums to a set to get the unique element 
        setA = set(nums)
        
        # create a set consisting of the original elements for this range
        setB = {i for i in range(1,len(nums)+1)}
        
        # return the difference of elements which are in setB but not in setA. Note that `setA - setB` wont work in this case
        return(setB - setA)