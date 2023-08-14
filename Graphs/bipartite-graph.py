# https://practice.geeksforgeeks.org/problems/bipartite-graph/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def isBipartite(self, V, adj):
        # code here
        def color(colored, node, adj, colour):
            colored[node] = colour
            for ele in adj[node]:
                if colored[ele] == -1:
                    if color(colored, ele, adj, 1 - colour):
                        return True
                elif colored[node] == colored[ele]:
                    return True
            return False

        colored = [-1 for i in range(V)]
        for i in range(V):
            if colored[i] == -1:
                if color(colored, i, adj, 1):
                    return False
        return True


# {
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends