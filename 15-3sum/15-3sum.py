class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        """
        Approach
        1. If len of the nums <=2, it means it does not have a triplet, so we can return []
        2. Else, sort the nums array to that we can proceed furhter. This will take nlog(n) time
        3. Linearly iterate over the list form the first item till second last element, and set the low and high pointers to low +1 and len(arr) resp
        4. set the low pointer as i+1 and high pointer as end of the list
        5. repeat till low < high
        6. if sum of three nums == 0 , add that element to the list, sort it and add them to a set (as we need to return the unique set)
        7. If the sum of three nums < 0, it means we need to move towards right, so decrement the high pointer
        8. If the sum of three nums > 0, it means we need to move towards left, so increment the low pointer
        9. Return result set
        
        Time complexity = Sorting the array takes O(nlogn), so overall complexity is (n\log{n} + n^2  This is asymptotically equivalent to (n^2)
        Space complexity: O(n) for using set
        """
        # special case
        if len(nums) <= 2:
            return []

        result = set()  # result will contain the unique tuples

        nums = sorted(nums) # nlog(n) complexity

        for x in range(len(nums)-2):
            b = x+1          # begining pointer points to next
            e = len(nums)-1  # end pointer points to last element in nums

            while b < e: # while pointers don't cross one another
                val = nums[x]+ nums[b] + nums[e]
                if val == 0: # we have found the sum
                    result.add(tuple(sorted((nums[x],nums[b],nums[e])))) # need to convert to tuple as it's immutable

                    b += 1
                    e -= 1

                if val < 0: # we need to increase the result, so move towards the right side
                    b += 1
                if val > 0:  # we need to decrease the result, so move towards the left side
                    e -= 1
        return result
                        
            
