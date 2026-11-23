class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest= prices[0]
        profit= 0
        for price in prices:
            lowest= min(lowest, price)
            profit= max(profit-lowest, profit)
        return profit