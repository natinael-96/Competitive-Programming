# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)
        visited[0] = True

        def dfs(node):
            for nd in rooms[node]:
                if not visited[nd]:
                    visited[nd] = True
                    dfs(nd)

        dfs(0)

        return False not in visited