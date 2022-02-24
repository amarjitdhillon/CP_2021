class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        colors = {0:[1,2], 1:[0,2], 2:[0,1]}
        
        # here color is the selected color's index and n is the current house index (in 0 indexed array)
        def findCost(n,color):
            # return result from the momoization dict
            if (n,color) in self.memo:
                return self.memo[(n,color)]
            
            # get the current cost
            cost = costs[n][color]
            
            # base case: when we reach the leaf of the tree
            if n == len(costs)-1 :
                return cost
                        
            # get the alternative colors, based on the curretn color
            secondColor = colors.get(color)[0]
            thirdColor  = colors.get(color)[1]
            
            # The cost wil be minimum we get from using alternative colors
            cost += min(findCost(n+1, secondColor), findCost(n+1, thirdColor)) 
            
            # save memo dict
            self.memo[(n,color)] = cost
            
            return cost
        
        if costs == []:
            return 0
        
        # memo is dict used for memoization 
        self.memo = {}
        
        # total cost will be least cost by choosing to color the first house by red, blue and green
        return min(findCost(0,0), findCost(0,1), findCost(0,2))

