# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getTree(self,nums):
        if len(nums)==0:
            return
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.getTree(nums[:mid])
        root.right=self.getTree(nums[mid+1::])
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getTree(nums)