# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        g = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp: 
                graph[x].append(y)
                graph[y].append(x)
                if x in g: 
                    queue.add(x)
                if y in g: 
                    queue.add(y)
                    
            queue = deque(queue)
            while queue: 
                x = queue.popleft()
                for y in graph[x]: 
                    if y not in g: 
                        g.add(y)
                        queue.append(y)
        return g