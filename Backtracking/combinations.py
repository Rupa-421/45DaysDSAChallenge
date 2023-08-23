class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(remain,comb,next):
            if remain==0:
                res.append(comb[::])
            else:
                for i in range(next,n+1):
                    comb.append(i)
                    backtrack(remain-1,comb,i+1)
                    comb.pop()
        backtrack(k,[],1)
        return res