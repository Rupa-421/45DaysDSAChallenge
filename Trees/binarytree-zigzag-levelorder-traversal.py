# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[root]
        res=[[root.val]]
        reverse=True
        while len(q):
            next_level=[]
            next_level_vals=[]
            while len(q):
                node=q.pop(0)
                if node.left:
                    next_level.append(node.left)
                    next_level_vals.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_vals.append(node.right.val)
            if reverse==False and len(next_level_vals):
                res.append(next_level_vals)
                reverse=True
            elif len(next_level_vals):
                res.append(next_level_vals[::-1])
                reverse=False
            q=next_level
        print(res)
        return res
