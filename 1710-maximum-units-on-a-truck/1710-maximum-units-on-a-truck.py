class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort the truck as per the second item in the boxTypes in the reverse order
        sortedBoxTypes = sorted(boxTypes, key= lambda x:x[1],reverse = True )
        
        # initialize variables
        pending, number_of_units = truckSize, 0
        
        # loop over the sortedBoxTypes
        for count, cost in sortedBoxTypes:
            if (pending > 0):
                # If we still have the space, we will add the boxes one by one
                for i in range(1,count+1):
                    if pending  > 0:
                        # update the result
                        number_of_units += cost   
                        # decrement the counter
                        pending -= 1
            else:
                return number_of_units
        return number_of_units
        
        