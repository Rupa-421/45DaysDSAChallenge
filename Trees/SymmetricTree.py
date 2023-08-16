# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/symmetric-tree/description/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(root1,root2):
            if root1 and root2:
                if root1.val!=root2.val:
                    return False
                else:
                    return mirror(root1.left,root2.right) and mirror(root1.right,root2.left)
            elif root1 or root2:
                return False
            else:
                return True
        return mirror(root.left,root.right)