#https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def add(index1, nums1, val):
            prevval = val
            for i in range(index1, len(nums1)):
                nextval = nums1[i]
                nums1[i] = prevval
                prevval = nextval

        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                index1 += 1
            else:
                add(index1, nums1, nums2[index2])
                index1 += 1
                index2 += 1
        filled = n - index2
        print(nums1, index2)
        while index2 < n:
            nums1[len(nums1) - filled] = nums2[index2]
            index2 += 1
            filled -= 1
            # print(index2,filled,n,nums1)



