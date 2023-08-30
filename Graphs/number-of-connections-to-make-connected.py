from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        graph=[[] for i in range(n)]
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        vis=[False for i in range(n)]
        def dfs(i):
            if vis[i]==True:
                return 0
            vis[i]=True
            if graph[i]:
                for j in graph[i]: dfs(j)
            return 1
        return sum(dfs(i) for i in range(n))-1