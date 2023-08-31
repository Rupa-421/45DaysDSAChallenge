class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[]
        rank={val:i+1 for i,val in enumerate(sorted(set(nums)))}
        n=len(nums)
        bit=[0]*(n+1)
        def update(i):
            while i<=n:
                bit[i]+=1
                i+=(i&-i)
        def getsum(i):
            s=0
            while i:
                s+=bit[i]
                i-=(i&-i)
            return s
        for x in nums[::-1]:
            res.append(getsum(rank[x]-1))
            update(rank[x])
        return res[::-1]