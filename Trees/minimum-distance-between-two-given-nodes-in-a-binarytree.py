class Solution:
    def getLca(self,root,a,b):
        if root:
            if root.data==a or root.data==b:
                return root
            left=self.getLca(root.left,a,b)
            right=self.getLca(root.right,a,b)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
    def getHeight(self,q,a,res):
        while q:
            found=False
            newq=[]
            while q:
                root=q.pop(0)
                if root.data==a:
                    found=True
                    break
                if root.left:
                    newq.append(root.left)
                if root.right:
                    newq.append(root.right)
            if found==False:
                res+=1
                q=newq
            else:
                break
        # print(res)
        return res
    def findDist(self,root,a,b):
    
        #return: minimum distance between a and b in a tree with given root
        #code here
        parent=self.getLca(root,a,b)
        # print(parent.data)
        q=[parent]
        res=[0]
        res[0]+=self.getHeight(q,a,0)
        q=[parent]
        res[0]+=self.getHeight(q,b,0)
        return res[0]