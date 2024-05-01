# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        car = 0
        ans = ""

        a, b = list(a), list(b)
        while a or b or car:
            cur = car
            if a:
                cur += int(a.pop())
            if b:
                cur += int(b.pop())
            
            car = cur//2
            cur %= 2

            ans += str(cur)
        return ans[::-1]