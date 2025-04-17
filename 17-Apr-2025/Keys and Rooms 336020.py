# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0 for _ in range(len(rooms))]
        def dfs(node):
            for n in rooms[node]:
                if not visited[n]:
                    visited[n] = 1
                    dfs(n)
        visited[0] = 1
        dfs(0)
        for i in range(len(rooms)):
            if not visited[i]:
                return False
        return True
