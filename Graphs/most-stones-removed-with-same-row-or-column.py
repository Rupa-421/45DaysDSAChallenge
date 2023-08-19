class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_axis={}
        y_axis={}
        for stone in stones:
            if stone[0] in x_axis:
                x_axis[stone[0]].append(stone[1])
            else:
                x_axis[stone[0]]=[stone[1]]
            if stone[1] in y_axis:
                y_axis[stone[1]].append(stone[0])
            else:
                y_axis[stone[1]]=[stone[0]]
        # print(x_axis,y_axis)
        def rec(x,y,visited):
            for adj in x_axis[x]:
                if (x,adj) not in visited:
                    visited.add((x,adj))
                    rec(x,adj,visited)
            for adj in y_axis[y]:
                if (adj,y) not in visited:
                    visited.add((adj,y))
                    rec(adj,y,visited)
            # print(visited,x,y,res)

                
        visited=set()
        ans=0
        for stone in stones:
            if (stone[0],stone[1]) not in visited:
                visited.add((stone[0],stone[1]))
                rec(stone[0],stone[1],visited)
                ans+=1
        return len(stones)-ans