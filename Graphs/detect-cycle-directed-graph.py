#https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
class Solution:

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        state=[0]*V
        def cyclic(v):
            if state[v]==1:
                return False
            if state[v]==-1:
                return True
            state[v]=-1
            for i in adj[v]:
                if cyclic(i):
                    return True
            state[v]=1
            return False
        for i in range(V):
            if cyclic(i):
                return True
        return False
