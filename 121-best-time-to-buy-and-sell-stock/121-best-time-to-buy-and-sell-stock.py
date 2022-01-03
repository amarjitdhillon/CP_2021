class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        '''
        Here we can use 2 variables while doing the linear traversal
        1. minValue: to hold the min val at which we can buy
        2. maxProfit: at every step we can upaate the profit if it's more
        '''
        
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
                continue
            
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        
        return maxProfit
    
    '''
    Time complexity: O(n) as we are doing a single pass
    Space complexity: O(1) as we are using 2 variables
    '''

        