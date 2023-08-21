#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructTree(self,preorder,postorder,preStart,preEnd,postStart,postEnd):
        if preStart>preEnd: return None
        root=TreeNode(preorder[preStart])
        if(preStart==preEnd): return root
        postIndex=postStart
        while(postorder[postIndex]!=preorder[preStart+1]): postIndex+=1
        length=postIndex-postStart+1
        root.left=self.constructTree(preorder,postorder,preStart+1,preStart+length,postStart,postIndex)
        root.right=self.constructTree(preorder,postorder,preStart+length+1,preEnd,postIndex+1,postEnd)
        return root
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.constructTree(preorder,postorder,0,len(preorder)-1,0,len(postorder)-1)