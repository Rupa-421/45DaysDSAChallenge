class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size=len(cardPoints)-k
        maxi=float('inf')
        cursum=0
        start=0
        for i,v in enumerate(cardPoints):
            cursum+=v
            if i-start+1>size:
                cursum-=cardPoints[start]
                start+=1
            if i-start+1==size:
                maxi=min(maxi,cursum)
        return sum(cardPoints)-maxi
            