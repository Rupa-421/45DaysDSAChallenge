# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self,root,res):
        if root is None:
            return 0
        left=self.findMax(root.left,res)
        right=self.findMax(root.right,res)
        singlemax=max(root.val,max(left,right)+root.val)
        totalmax=max(singlemax,root.val+left+right)
        res[0]=max(res[0],totalmax)
        return singlemax
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[float('-inf')]
        self.findMax(root,res)
        return res[0]