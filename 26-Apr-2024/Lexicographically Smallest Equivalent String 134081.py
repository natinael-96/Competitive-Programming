# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        un = {i:i for i in map(chr, range(ord('a'), ord('z') + 1))}
        n = len(s1)

        def find(x):
            while un[x] != x:
                un[x] == un[un[x]]
                x = un[x]
            return x
        
        for i in range(n):
            r1, r2 = find(s1[i]), find(s2[i])

            if r1 < r2:
                un[r2] = r1
            else:
                un[r1] = r2

        ans = ''
        for i in baseStr:
            ans += (find(i))
            #print(find(i))
        
        return ans