# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution:
    def reverseWords(self, s: str) -> str:
        words=""
        word=""
        reverse=s[::-1]
        for i,char in enumerate(reverse):
            # print(char)
            if char!=" " and word!="" and reverse[i-1]==" ":
                words+=(word+" ")
                word=char
            elif char!=" ":
                word=(char+word)
            else:
                continue
        if word!="":
            words+=word
        return words
