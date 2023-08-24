class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        res=[0]
        def inorder(root,low,high,res):
            if root:
                inorder(root.left,low,high,res)
                if root.data>=low and root.data<=high:
                    res[0]+=1
                inorder(root.right,low,high,res)
        inorder(root,low,high,res)
        return res[0]