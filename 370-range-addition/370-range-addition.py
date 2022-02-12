class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length+1)
        for start, end, value in updates:
            arr[start] += value
            arr[end+1] -= value
        
        for x in range(1, length+1):
            arr[x] += arr[x-1]
        
        return arr[:length]