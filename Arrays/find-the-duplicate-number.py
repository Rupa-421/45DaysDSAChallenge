class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo=1
        hi=len(nums)-1
        while hi-lo>1:
            mid=(lo+hi)//2
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            # print(count,lo,mid,high)
            if count>mid:
                hi=mid
            else:
                lo=mid+1
        count=0
        for num in nums:
            if num<=lo:
                count+=1
        if count>lo:
            return lo
        else:
            return hi