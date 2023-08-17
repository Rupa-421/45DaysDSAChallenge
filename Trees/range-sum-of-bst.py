
# https://leetcode.com/problems/range-sum-of-bst/description/
#/ Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if not root:
            return ans
        if root.val > low:
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            ans += root.val
        return ans
