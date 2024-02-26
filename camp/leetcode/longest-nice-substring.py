class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) == 1:
            return ""
        
        st = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in st:
                break

        else:
            return s

        s1 = self.longestNiceSubstring(s[:i])
        s2 = self.longestNiceSubstring(s[i+1:])

        if len(s1) >= len(s2):
            return s1
        else:
            return s2
