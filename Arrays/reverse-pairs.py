class Solution:
    def update(self,bit,index,x):
        while index<len(bit):
            bit[index]+=x
            index+=(index&-index)
    def sumof(self,bit,index):
        total=0
        while index>0:
            total+=bit[index]
            index-=(index&-index)
        return total

    def reversePairs(self, nums: List[int]) -> int:
        total=nums+[x*2 for x in nums]
        sortednums=list(sorted(set(total)))
        bit=[0 for i in range(len(sortednums)+1)]
        res=0
        rank={}
        for ind,val in enumerate(sortednums):
            rank[val]=ind+1
        for i in nums[::-1]:
            res+=self.sumof(bit,rank[i]-1)
            self.update(bit,rank[2*i],1)
        return res