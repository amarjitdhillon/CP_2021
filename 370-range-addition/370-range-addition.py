class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Initialize an array of length+1 with all values as 0
        arr = [0] * (length+1)
        
        # Iterate over all the given ranges
        for start, end, value in updates:
            '''
            Just update the start index with +val and end+1 with -val as we need to see the effect till end
            We will use the prefix sum to retrive the actual sum, later
            '''
            arr[start] += value
            arr[end+1] -= value
        
        # Iterte over the array again and get the prefix sum. This time we need to iterate form second element onwards
        for x in range(1, length+1):
            arr[x] += arr[x-1]
        
        '''
        We do not need to return the last element as we have already created this array with one extra size. 
        This extra size was to do the prefix sum and access the end+1 index
        '''
        return arr[:length]