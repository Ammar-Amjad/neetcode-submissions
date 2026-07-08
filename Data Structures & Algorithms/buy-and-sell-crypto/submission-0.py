class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_p = prices[-1]
        max_p = prices[-1]
        best_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] <= min_p:
                min_p = min(min_p, prices[i])   
                best_profit = max(best_profit, max_p - min_p) 
            else:
                max_p = max(max_p, prices[i]) 
                min_p = prices[i] 

        return best_profit