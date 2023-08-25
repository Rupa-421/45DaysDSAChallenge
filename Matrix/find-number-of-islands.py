#User function Template for python3

#User function Template for python3
from collections import deque
class Solution:
    def issafe(self,i,j,r,c,grid,vis):
        if 0<=i<r and 0<=j<c and grid[i][j] and vis[i][j]==False:
            return True
        return False
    def bfs(self,grid,vis,i,j):
        row=[0,0,1,-1,1,-1,1,-1]
        col=[1,-1,0,0,-1,1,1,-1]
        q=deque()
        q.append([i,j])
        vis[i][j]=True
        while q:
            temp=q.popleft()
            ti=temp[0]
            tj=temp[1]
            for k in range(8):
                if self.issafe(ti+row[k],tj+col[k],len(grid),len(grid[0]),grid,vis):
                    vis[ti+row[k]][tj+col[k]]=True
                    q.append([ti+row[k],tj+col[k]])
    def numIslands(self,grid):
        #code here
        count=0
        vis=[[False for i in range(len(grid[0]))]for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and vis[i][j]==False:
                    self.bfs(grid,vis,i,j)
                    count+=1
        return count