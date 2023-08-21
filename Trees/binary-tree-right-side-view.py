# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-right-side-view/description/
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,depth,set_of_nodes):
            if root:
                if depth not in set_of_nodes:
                    set_of_nodes[depth]=root.val
                preorder(root.right,depth+1,set_of_nodes)
                preorder(root.left,depth+1,set_of_nodes)
        set_of_nodes={}
        preorder(root,0,set_of_nodes)
        res=[]
        for i in sorted(set_of_nodes):
            res.append(set_of_nodes[i])
        return res