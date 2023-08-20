# https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(len(nums) - 1):
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                else:
                    k -= 1

        return [list(ans) for ans in res]