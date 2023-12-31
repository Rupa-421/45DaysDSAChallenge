class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        r=len(matrix[0])
        t=0
        b=len(matrix)
        res=[]
        while l<r and t<b:
            for i in range(l,r,1):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b,1):
                res.append(matrix[i][r-1])
            r-=1
            if t<b:
                for i in range(r-1,l-1,-1):
                    res.append(matrix[b-1][i])
                b-=1
            if l<r:
                for i in range(b-1,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res