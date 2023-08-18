# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcDepth(self,root,maxDepth,depth):
        if root:
            maxDepth[0]=max(maxDepth[0],depth)
            self.calcDepth(root.left,maxDepth,depth+1)
            self.calcDepth(root.right,maxDepth,depth+1)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth=[0]
        self.calcDepth(root,maxDepth,1)
        return maxDepth[0]