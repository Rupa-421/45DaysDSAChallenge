# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/validate-binary-search-tree/description/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,mini,maxi):
            if root:
                if mini<root.val<maxi:
                    return valid(root.left,mini,root.val) and valid(root.right,root.val,maxi)
                else:
                    return False
            else:
                return True
        return valid(root,-float('inf'),float('inf'))