# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                res.append(abs(nums[i]))
            nums[abs(nums[i])-1]=-(nums[abs(nums[i])-1])
        return res