class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elements=set()
        index=0
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements.add(nums[i])
                nums[index]=nums[i]
                index+=1
        return index