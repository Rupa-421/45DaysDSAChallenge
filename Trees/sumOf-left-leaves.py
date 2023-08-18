# https://leetcode.com/problems/sum-of-left-leaves/description/
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def preorder(root,sum):
            if root:
                if root.left and root.left.left==None and root.left.right==None:
                    sum[0]+=root.left.val
                preorder(root.left,sum)
                preorder(root.right,sum)
        sum=[0]
        preorder(root,sum)
        return sum[0]