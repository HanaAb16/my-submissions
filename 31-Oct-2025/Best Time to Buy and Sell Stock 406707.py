# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        buy = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit , price - buy)
            buy = min(buy , price)
        return profit
        