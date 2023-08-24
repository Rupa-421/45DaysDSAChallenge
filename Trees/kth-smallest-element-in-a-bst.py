# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_count=[0]
        res=[0]
        def inorder(root,node_count,res):
            if root:
                inorder(root.left,node_count,res)
                node_count[0]+=1
                if node_count[0]==k:
                    res[0]=root.val
                inorder(root.right,node_count,res)
        inorder(root,node_count,res)
        return res[0]