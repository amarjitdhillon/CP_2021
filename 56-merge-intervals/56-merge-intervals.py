class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals by the start value, in case they are not sorted by default
        intervals.sort(key = lambda x: x[0])
        
        # edge case. If num elements is one, then return the same list
        if len(intervals) == 1:
            return intervals
        
        # add the first element to the result list
        result = [intervals[0]]
        
        # loop over the second element onwards as first is already added to result list
        for start, end in intervals[1:]:
            
            # get the prev end value from the result array
            prevEnd = result[-1][1]
            
            # if the start of this element is <= the prevEnd, then take the max from both's end and expand the interval
            if  start <= prevEnd:
                # update the end in result
                result[-1][1] = max(end,prevEnd)
            else:
                result.append([start,end])
                
        # else return the result
        return result