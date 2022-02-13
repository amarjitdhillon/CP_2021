class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
        hashmap will store the next greater element
        ngeStack will hold the elements in monotonic increasing from the top to bottom. 
        result will hold the final result we want to output
        '''
        ngeHashMap, ngeStack, res =  {} , [], []
        
        for x in nums2:
            while ngeStack and x > ngeStack[-1]:
                # if we encounter the greater element, then we can set it as nge for top element
                ngeHashMap[ngeStack.pop()] = x
            ngeStack.append(x)
            
        # Step2: iterate over nums1 and populate result based of the k,v in ngeHashMap
        for y in nums1:
            if y not in ngeHashMap:
                res.append(-1)
            else:
                res.append(ngeHashMap.get(y))
        
        return res
        