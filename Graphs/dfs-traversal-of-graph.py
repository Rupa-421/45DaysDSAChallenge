
class Solution:
    def dfs(self,visited,v,adj,res):
        visited.add(v)
        res.append(v)
        for nei in adj[v]:
            if nei not in visited:
                self.dfs(visited,nei,adj,res)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited=set()
        res=[]
        self.dfs(visited,0,adj,res)
        return res