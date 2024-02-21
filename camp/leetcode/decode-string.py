class Solution:
    def decodeString(self, s: str) -> str:
        
        out = ""
        prev = 0
        rep = 0
        opB =0

        for i in range(len(s)):
            if opB == 0 and  s[i]  >= "a" and s[i] <= "z":
                out += s[i]
                prev = i + 1
            if s[i] == "[":
                opB += 1
                if opB == 1:
                    rep = 0
                    for j in s[prev:i]:
                        rep = rep * 10 + int(j)
                    prev = i + 1
            elif s[i] == "]":
                opB -= 1

                if opB == 0:
                    while rep > 0:
                        out += self.decodeString(s[prev:i])
                        rep -= 1
                    prev = i + 1
        return out
    


