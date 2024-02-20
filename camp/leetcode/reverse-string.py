class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def rev(strg, l):
            if l == len(strg)//2:
                return 
            
            strg[l], strg[len(strg) - l -1] = strg[len(strg) - l -1], strg[l]
            
            rev(strg, l + 1)
        rev(s, 0)