class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=Counter()
        res=maxf=0
        for i in range(len(s)):
            count[s[i]]+=1
            maxf=max(maxf,count[s[i]])
            if res-maxf<k:
                res+=1
            else:
                count[s[i-res]]-=1
        return res