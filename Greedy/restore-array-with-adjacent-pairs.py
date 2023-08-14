class Solution:
    def dfs(self,start,adj,res,visited):
        res.append(start)
        visited.add(start)
        if start in adj:
            for ele in adj[start]:
                if ele not in visited:
                    self.dfs(ele,adj,res,visited)
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacency_list={}
        for edge in adjacentPairs:
            if edge[0] not in adjacency_list:
                adjacency_list[edge[0]]=[edge[1]]
            else:
                # print(adjacency_list)
                adjacency_list[edge[0]].append(edge[1])
            if edge[1] not in adjacency_list:
                adjacency_list[edge[1]]=[edge[0]]
            else:
                adjacency_list[edge[1]].append(edge[0])
        start=0
        for ele in adjacency_list:
            if len(adjacency_list[ele])==1:
                start=ele
        res=[]
        visited=set()
        self.dfs(start,adjacency_list,res,visited)
        return res