class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini=strs[0]
        mini_len=len(mini)
        for i in range(1,len(strs)):
            if len(strs[i])<mini_len:
                mini=strs[i]
                mini_len=len(strs[i])
        index=0
        flag=True
        res=""
        while index<mini_len:
            for i in range(len(strs)):
                if strs[i][index]!=mini[index]:
                    flag=False
                    break
            if flag==False:
                break
            else:
                res+=mini[index]
                index+=1
            
        return res