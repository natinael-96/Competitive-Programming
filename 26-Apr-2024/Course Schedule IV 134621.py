# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False]*len(queries)

        graph = defaultdict(list)
        deg = defaultdict(int)

        for a, b in prerequisites:
            graph[a].append(b)
            deg[b] += 1
        
        q = deque()
        for i in graph.keys():
            if deg[i] == 0:
                q.append(i)
        
        reqs = [set([i]) for i in range(numCourses)]

        while q:
            node = q.popleft()
            for nei in graph[node]:
                
                for i in reqs[node]:
                    reqs[nei].add(i)
                
                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        
        ans = []
        for a, b in queries:
            ans.append(a in reqs[b])
        
        return ans 





        