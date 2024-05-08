# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dicT = defaultdict(int)

        for w in words:
            for i in w:
                dicT[w] |= 1 << (ord(i) - ord('a'))
        
        ans = 0
        for i in dicT.keys():
            for j in dicT.keys():
                if dicT[i] & dicT[j] == 0:
                    ans = max(ans, len(i)*len(j))
        
        return ans