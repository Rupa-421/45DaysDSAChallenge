class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache,stack,result={},[],[]
        for i in nums2:
            while stack and stack[-1]<i:
                cache[stack.pop()]=i
            stack.append(i)
        for i in nums1:
            result.append(cache.get(i,-1))
        return result