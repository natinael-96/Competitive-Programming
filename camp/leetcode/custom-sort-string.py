class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = Counter(s)

        ans = []
        for i in order:
            ans.append(i * count[i])
            del count[i]
        for i in count.keys():
            ans.append( i * count[i])
        return ''.join(ans)