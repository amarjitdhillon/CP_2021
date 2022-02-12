class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a dp array for 0 to amount (inclusive) with the max values
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        # let's compute dp array for all values from 1 to amount
        for i in range(1, amount+1):
            # we will consider all the coins and then take min from that
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        # after this loop is run, dp[amount] is our result given the fact that it's not inf
        # if it's inf, then we will return -1
        return dp[amount] if dp[amount] != float('inf') else -1
        
        
        