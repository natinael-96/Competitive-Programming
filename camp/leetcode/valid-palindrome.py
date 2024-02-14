class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        for i in s:
            if i.isalnum():
                st.append(i.lower())
                
        return st[:] == st[::-1]