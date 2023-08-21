# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack=[]
        dup=root
        while root:
            if root.right:
                stack.append(root.right)
            root.right=root.left
            root.left=None
            if root.right==None and len(stack)!=0:
                root.right=stack.pop()
            root=root.right
        return dup