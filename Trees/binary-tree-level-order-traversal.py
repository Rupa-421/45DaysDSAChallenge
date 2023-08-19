# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        if root is None:
            return []
        q = [root]
        while len(q) != 0:
            newq = []
            res = []
            while len(q) != 0:
                node = q.pop(0)
                res.append(node.val)
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            q = newq
            level.append(res)
        return level
