class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        snums = set(nums)
        self.res = ""
        self.found = False
        
        def dfs(x: str):
            # base case for leaf nodes
            if len(x) == len(nums):
                # if the valid string is not found in the set, it means this sting is missing
                if x not in snums:  
                    # save this sting and stop the recursion
                    self.res = x 
                    self.found = True
             
            # condition to stop further recursion
            if self.found:
                return
            
            # base case: returning from leaf nodes
            if len(x) > len(nums):
                return True
            
            # call both the possibilities with appended "0" and "1"
            dfs(x+"0")
            dfs(x+"1")
            
        # driver code 
        dfs("") 
        return self.res
