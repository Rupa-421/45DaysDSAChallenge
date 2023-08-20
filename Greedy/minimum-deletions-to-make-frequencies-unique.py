class Solution:
    def minDeletions(self, s: str) -> int:
        count=Counter(s)
        li=[]
        for ele in count: li.append(count[ele])
        li.sort(reverse=True)
        res=0
        for i in range(1,len(li)):
            if li[i]>li[i-1]:
                res+=(li[i]-li[i-1])
                li[i]=li[i-1]
            if li[i]==li[i-1] and li[i-1]!=0:
                res+=1
                li[i]-=1
        return res
