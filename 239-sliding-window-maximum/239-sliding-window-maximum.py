class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we will maintain the queue in monotinic decreasing fashion, so that left value in the deque is always the max one
        w, res = deque() , []
        
        for i,x in enumerate(nums):
            # If the current element is greater then the right most element in the deque, then remove it. 
            # Do it till the current element is less then the last element in the deque
            while w and  x >= w[-1][1]:
                w.pop()
                
            # if the current index - index of the left most item in deque is >= K, it means that pair is invalid, so remove it
            while w and i - w[0][0] >= k:
                w.popleft()    
                
            # add the index and value pair as tuple at the end of the deque
            w.append((i,x))
            
            # as the array is 0 based so, when i == k-1, then first window is found. Hence return the max value in the window which is the first value in the dequue
            if i >= k-1:
                res.append(w[0][1])
        return res
    
                
            