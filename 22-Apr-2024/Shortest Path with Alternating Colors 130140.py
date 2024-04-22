# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        ans = [-1]*n
        
        for i, j in redEdges:
            graph[i].append((j, 'r'))
        
        for i, j in blueEdges:
            graph[i].append((j, 'b'))


        q = deque([(0, 0, '')])

        visited = set()

        while q:
            cur, l, color = q.popleft()

            if (cur, color) not in visited:
                visited.add((cur, color))

                if ans[cur] == -1:
                    ans[cur] = l

                for nxtNm, nxtCol in graph[cur]:
                    if color != nxtCol:
                        q.append((nxtNm, l + 1, nxtCol))

        return ans
