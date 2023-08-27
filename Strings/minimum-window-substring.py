from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter=Counter(t)
        mini=float('inf')
        res=""
        count=len(counter)
        start=0
        end=0
        while end<len(s):
            if s[end] in counter:
                counter[s[end]]-=1
                if counter[s[end]]==0:
                    count-=1
            while count==0 and start<=end:
                if end-start+1<mini:
                    mini=end-start+1
                    res=s[start:end+1:]
                if s[start] in counter:
                    counter[s[start]]+=1
                    if counter[s[start]]==1:
                        count+=1
                start+=1
            end+=1
        return res