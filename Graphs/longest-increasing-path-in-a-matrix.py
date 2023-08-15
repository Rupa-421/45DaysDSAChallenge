class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res=0
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0 for i in range(m)]for j in range(n)]
        def dfs(i,j,dp):
            if not dp[i][j]:
                val=matrix[i][j]
                dp[i][j]=1+max(dfs(i-1,j,dp) if i>0 and matrix[i-1][j]>val else 0,dfs(i+1,j,dp) if i+1<n and matrix[i+1][j]>val else 0,dfs(i,j-1,dp) if j>0 and matrix[i][j-1]>val else 0,dfs(i,j+1,dp) if j+1<m  and matrix[i][j+1]>val else 0)
            return dp[i][j]
        for i in range(n):
            for j in range(m):
                res=max(res,dfs(i,j,dp))
        return res

                