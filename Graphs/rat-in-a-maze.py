# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution:
    def findPath(self, m, n):
        # code here
        def dfs(m, n, i, j, stack, res, visited):
            if i >= n or j >= n or i < 0 or j < 0:
                return
            if m[i][j] == 0 or visited[i][j] == 1:
                return
            elif i == n - 1 and j == n - 1:
                res.append(''.join(stack))
                stack = []
                visited[i][j] = 0
                return
            else:
                visited[i][j] = 1
                stack.append('U')
                dfs(m, n, i - 1, j, stack, res, visited)
                stack.pop()
                stack.append('D')
                dfs(m, n, i + 1, j, stack, res, visited)
                stack.pop()
                stack.append('L')
                dfs(m, n, i, j - 1, stack, res, visited)
                stack.pop()
                stack.append('R')
                dfs(m, n, i, j + 1, stack, res, visited)
                stack.pop()
                visited[i][j] = 0
                return

        stack = []
        res = []
        visited = [[0 for i in range(n)] for j in range(n)]
        dfs(m, n, 0, 0, stack, res, visited)
        if res:
            res.sort()
            return res
        else:
            return [-1]
