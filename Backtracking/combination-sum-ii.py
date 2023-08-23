class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res,target,candidates,ind,path):
            if target==0:
                res.append(path)
            elif target<0:
                return 
            else:
                for i in range(ind,len(candidates)):
                    if i>ind and candidates[i]==candidates[i-1]: continue
                    backtrack(res,target-candidates[i],candidates,i+1,path+[candidates[i]])
        candidates.sort()
        res=[]
        backtrack(res,target,candidates,0,[])
        return res