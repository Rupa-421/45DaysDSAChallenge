#User function Template for python3
from collections import defaultdict
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        res=[0]
        graph=defaultdict(list)
        for i in range(V):
            if adj[i]!=[]:
                graph[i]=adj[i]
        q=[0]
        visited={0}
        while q:
            newq=[]
            while q:
                node=q.pop(0)
                if node in graph:
                    for x in graph[node]:
                        if x not in visited:
                            visited.add(x)
                            newq.append(x)
            q=newq
            if len(newq)!=0:
                res+=newq
        return res