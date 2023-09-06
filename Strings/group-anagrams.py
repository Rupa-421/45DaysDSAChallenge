class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorting=[]
        anagrams={}
        for i in strs:
            p=''.join(sorted(i))
            if p not in sorting:
                sorting+=[p]
                anagrams[p]=[i]
            else:
                anagrams[p].append(i)
        return (list(anagrams.values()))