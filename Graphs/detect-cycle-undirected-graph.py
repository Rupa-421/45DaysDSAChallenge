from typing import List
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        state = [False for i in range(V)]

        def cyclic(node, parent):
            state[node] = True
            for nei in adj[node]:
                if state[nei] == False:
                    if cyclic(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False

        for node in range(V):
            if state[node] == False:
                if cyclic(node, -1):
                    return True

    return False
