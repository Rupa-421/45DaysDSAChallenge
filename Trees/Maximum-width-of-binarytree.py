# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        depth=0
        left=0
        q=[(root,0,0)]
        for node,curdepth,pos in q:
            if node:
                q.append([node.left,curdepth+1,2*pos+1])
                q.append([node.right,curdepth+1,2*pos+2])
                if curdepth!=depth:
                    depth=curdepth
                    left=pos
                ans=max(ans,(pos-left+1))
        return ans