class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={}
        totalsum=0
        count=0
        prefix[0]=1
        for i in range(len(nums)):
            totalsum+=nums[i]
            count+=prefix.get(totalsum-k,0)
            prefix[totalsum]=prefix.get(totalsum,0)+1
        return count
