# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def getParents(root):
            if root:
                if root.left:
                    root.left.parent=root
                if root.right:
                    root.right.parent=root
                getParents(root.left)
                getParents(root.right)
        root.parent=None
        getParents(root)

        list_of_res=[]
        def getNeiK(root,list_of_res,k,cur):
            if cur==k:
                if root:
                    list_of_res.append(root.val)
            if root:
                visited.add(root)
                if root.left not in visited:
                    getNeiK(root.left,list_of_res,k,cur+1)
                if root.right not in visited:
                    getNeiK(root.right,list_of_res,k,cur+1)
                if root.parent and root.parent not in visited:
                    getNeiK(root.parent,list_of_res,k,cur+1)
        visited=set()
        getNeiK(target,list_of_res,k,0)
        return list_of_res