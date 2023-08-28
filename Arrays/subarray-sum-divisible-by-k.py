class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        count=[1]+[0]*k
        prefix=0
        for ele in nums:
            prefix+=ele
            prefix%=k
            res+=count[prefix]
            count[prefix]+=1
        return res
