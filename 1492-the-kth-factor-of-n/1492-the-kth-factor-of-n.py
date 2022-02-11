class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # counter represent the i^th factor of the number found so far
        counter = 0
        
        # go over the number from 1 to n as we need to divide the n by this number to find if that number is a factor
        for i in range(1, n+1):
                        
            if n%i == 0:
                # increment the value of counter
                counter += 1
                
                # if the counter is equal to k, it means we have found the k^th factor
                if k == counter:
                    return i
                
        # if no factor is found then return -1        
        return -1