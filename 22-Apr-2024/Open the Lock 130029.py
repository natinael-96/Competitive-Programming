# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = deque()
        d = set(deadends)

        if '0000' not in d:
            q.append(('0000', 0))
            d.add('0000')
        
        while q:
            cur, mov = q.popleft()

            if cur == target:
                return mov
                
            for i in range(4):
                insrt = (int(cur[i])+ 1) % 10
                new = cur[:i] + str(insrt) + cur[i+1:]

                if new not in d:
                    d.add(new)
                    q.append((new, mov + 1))

                insrt = (int(cur[i])- 1) % 10
                new = cur[:i] + str(insrt) + cur[i+1:]

                if new not in d:
                    d.add(new)
                    q.append((new, mov + 1))

        return -1


                