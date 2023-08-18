# https://leetcode.com/problems/merge-two-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        newroot=None
        if root1 and root2:
            newroot=TreeNode(root1.val+root2.val)
            newroot.left=self.mergeTrees(root1.left,root2.left)
            newroot.right=self.mergeTrees(root1.right,root2.right)
        elif root1:
            newroot=root1
        elif root2:
            newroot=root2
        return newroot
