#https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ans = True
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) != 0:
                    before_char = stack.pop()
                    if (i == ']' and before_char == '[') or (i == '}' and before_char == '{') or (
                            i == ')' and before_char == '('):
                        pass
                    else:
                        ans = False
                        break
                else:
                    ans = False
                    break
        if ans == False or len(stack) != 0:
            return False
        else:
            return True
