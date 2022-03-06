class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # here remain is the remainingSum, arr is the array formed so far, idx is the id of the current num in candidates
        def dfs(remain, arr, idx):
            # base case: add the arr to the result array. Make a deep copy
            if remain == 0:
                result.append(list(arr))
                return 
            
            # base case: if the remain is < 0, then we need to backtrack
            if remain < 0:
                return
            
            # else explore all the possible cases
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                
                # explore all the possible cases from the current idx onwards
                dfs(remain - candidates[i], arr, i)
                
                # remove the last element
                arr.pop(-1)
                
            return result

        # driver code
        return dfs(target, [], 0)
            
        