class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0#prices[0]
        r = 1#prices[1]
        maxprofit = 0

        while r<len(prices):
            profit = prices[r]-prices[l]
            if profit > maxprofit:
                maxprofit = max(maxprofit, profit)

            if prices[r] < prices[l]:
                l = r
            else:
                r+=1
        return maxprofit
            
            