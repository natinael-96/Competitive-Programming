class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        ans = []

        def helper(opn, clos, path):

            if opn == clos == n:
                ans.append("".join(path[:]))
                return
            
            if opn < n:
                path.append('(')
                helper(opn +1, clos, path)
                path.pop()
            if clos < opn:
                path.append(')')
                helper(opn,clos + 1, path)
                path.pop()
        helper(0,0,[])

        return ans
