class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP= 0
        buy, sell = prices[0], -1
        

        for i in range(len(prices)):

            buy = min(prices[i], buy)
            sell = prices[i]

            profit = sell - buy
            maxP = max(profit, maxP)

        return maxP

