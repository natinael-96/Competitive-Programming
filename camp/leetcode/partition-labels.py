class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        wrds = defaultdict(int)
        for i,char in enumerate(s):
            wrds[char] = i
        
        lastIndx = wrds[s[0]]
        print(lastIndx)
        strt = 0
        ans = []
        for i, char in enumerate(s):
            
            lastIndx = max(wrds[char], lastIndx)

            if i == lastIndx:
                ans.append(lastIndx - strt + 1)
                lastIndx = wrds[char]
                strt = i + 1

        return ans