class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxTypes = sorted(boxTypes, key= lambda x:x[1],reverse = True )
        pending, number_of_units = truckSize, 0
        
        print(sortedBoxTypes)
        for count, cost in sortedBoxTypes:
            if (pending > 0):
                for i in range(1,count+1):
                    if pending  > 0:
                        number_of_units += cost   
                        pending -= 1
            else:
                return number_of_units
        return number_of_units
        
        