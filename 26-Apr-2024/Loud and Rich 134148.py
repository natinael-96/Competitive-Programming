# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        deg = [0]*len(quiet)
        adj = defaultdict(list)

        for a, b in richer:
            adj[a].append(b)
            deg[b] += 1

        ans = [i for i in range(len(quiet))]
        qu = quiet

        q = deque([i for i in range(len(deg)) if deg[i] == 0])

        while q:
            cur = q.popleft()

            for nei in adj[cur]:
                if qu[cur] < qu[nei]:
                    qu[nei] = qu[cur]
                    ans[nei] = ans[cur]

                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        return ans

