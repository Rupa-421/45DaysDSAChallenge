# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            else:
                profit=max(profit,prices[i]-mini)
        return profit