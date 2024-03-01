class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r = deque()
        d = deque()
        first = senate[0]
        for i in range(len(senate)):
            if senate[i] == "R": 
                r.append(i)
            else: 
                d.append(i)
        
        while r and d:
            currR = r.popleft()
            currD = d.popleft()

            if currR < currD:
                r.append(currR + len(senate))
            else:
                d.append(currD + len(senate))
        return "Radiant" if len(r) > 0 else "Dire"