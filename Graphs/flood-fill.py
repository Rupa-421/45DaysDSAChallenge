class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldval=image[sr][sc]
        q=[[sr,sc]]
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        visited=[[-1 for i in range(len(image[0]))]for j in range(len(image))]
        while q:
            node=q.pop(0)
            visited[node[0]][node[1]]=0
            image[node[0]][node[1]]=color
            for direction in directions:
                newx=node[0]+direction[0]
                newy=node[1]+direction[1]
                if newx>=0 and newy>=0 and newx<len(image) and newy<len(image[0]) and image[newx][newy]==oldval and visited[newx][newy]==-1:
                    q.append([newx,newy])
        return image

