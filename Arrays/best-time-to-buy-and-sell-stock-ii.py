class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0 for i in range(2)] for j in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for j in range(2):
                if j==0:
                    dp[i][j]=max(-prices[i]+dp[i+1][j+1],dp[i+1][j])
                else:
                    dp[i][j]=max(prices[i]+dp[i+1][j-1],dp[i+1][j])
        return dp[0][0]