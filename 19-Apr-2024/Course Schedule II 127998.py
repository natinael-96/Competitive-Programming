# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        WHITE = 0
        GREY = 1
        BLACK = 2
        
        graph = defaultdict(list)
        color = defaultdict(int)

        for a, b in prerequisites:
            graph[a].append(b)

        for i in range(numCourses):
            color[i] = WHITE

        ans = []
        cycle = [False]

        def dfs(node):

            if cycle[0]:
                return 
            if color[node] == WHITE:
                color[node] = GREY

                for nei in graph[node]:
                    if color[nei] == WHITE:
                        dfs(nei)
                    
                    elif color[nei] == GREY:
                        cycle[0] = True
                        return 
                color[node] = BLACK

                ans.append(node)

        for i in range(numCourses):
            dfs(i)

        return ans if not cycle[0] else []

        