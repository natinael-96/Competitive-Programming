class Solution:
    def longestPalindrome(self, s: str) -> int:
        elements = Counter(s)
        even = 0
        odd = 0

        for i in elements:
            if elements[i] % 2 == 0:
                even += elements[i]
            else:
                if odd == 0:
                    odd += elements[i]
                else:
                    odd += elements[i] - 1
        
        
        return even + odd


