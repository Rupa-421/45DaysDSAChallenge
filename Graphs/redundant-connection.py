# https://leetcode.com/problems/redundant-connection/description/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vertices=[i for i in range(len(edges)+1)]
        size=[1 for i in range(len(vertices)+1)]
        def find(x):
            if vertices[x]==x:
                return x
            else:
                vertices[x]=find(vertices[x])
                return vertices[x]
        def union(x,y):
            if size[x]>size[y]:
                vertices[y]=vertices[x]
                size[x]+=size[y]
            else:
                vertices[x]=vertices[y]
                size[y]+=size[x]

        for i,j in edges:
            iparent=find(i)
            jparent=find(j)
            if iparent==jparent:
                return [i,j]
            else:
                union(iparent,jparent)
            # print(vertices)