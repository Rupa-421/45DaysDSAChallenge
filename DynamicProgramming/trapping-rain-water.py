class Solution:
    def trap(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        water=0
        leftmax=0
        rightmax=0
        while start<end:
            leftmax=max(leftmax,height[start])
            rightmax=max(rightmax,height[end])
            if leftmax<rightmax:
                water+=leftmax-height[start]
                start+=1
            else:
                water+=rightmax-height[end]
                end-=1
        return water