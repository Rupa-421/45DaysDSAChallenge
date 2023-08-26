from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        p=Counter(nums)
        for i in p:
            if p[i]>n/2:
                return i