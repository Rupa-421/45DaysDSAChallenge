class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                leftstr=s[left:right]
                rightstr=s[left+1:right+1]
                return leftstr[::]==leftstr[::-1] or rightstr[::]==rightstr[::-1]
            left+=1
            right-=1
        return True