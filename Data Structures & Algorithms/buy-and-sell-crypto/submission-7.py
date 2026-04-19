class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        #minBuy: By updating this at every step, you ensure that for any given sell price, 
        #you are comparing it against the lowest possible price seen in the past.