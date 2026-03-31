class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        for i in range(len(prices)-1):
            
            future_prices = prices[i+1:]
            if current_max < max(future_prices) - prices[i]:
                current_max = max(future_prices) - prices[i]

        return current_max