class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=set()
        def backtrack(opens,close,str_):
            # print(opens,close,str_)
            if opens==0 and close==0:
                res.add(str_)
            else:
                if opens!=0:
                    backtrack(opens-1,close,str_+'(')
                if close >opens:
                    backtrack(opens,close-1,str_+')')
        backtrack(n,n,'')
        return [i for i in res]