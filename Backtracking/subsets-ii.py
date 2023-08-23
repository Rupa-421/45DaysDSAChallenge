class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(res,nums,ind,path):
            res.append(path)
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]: continue
                dfs(res,nums,i+1,path+[nums[i]])

        nums.sort()
        res=[]
        dfs(res,nums,0,[])
        return res