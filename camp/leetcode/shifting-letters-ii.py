class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shif = [0]*(len(s)+1)

        for i in (shifts):
            a,e,d = i[0], i[1], i[2]
            if d:
                shif[a] += 1
                shif[e+1] -= 1
            else:
                shif[a] -= 1
                shif[e + 1] -= -1
        for i in range(1,len(shif)):
            shif[i] += shif[i-1]
        ans = ''
        for i in range(len(s)):
            ans += chr((ord(s[i]) + shif[i] - ord('a'))%26 + ord('a') )
            
        return ans